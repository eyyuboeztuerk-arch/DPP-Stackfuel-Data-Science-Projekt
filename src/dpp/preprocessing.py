"""
dpp/preprocessing.py

Robust preprocessing implementation:
- loads CSV (default path or custom csv_path)
- separates target / features
- detects numeric and categorical columns
- builds ColumnTransformer with StandardScaler + OneHotEncoder
  (compatible with older/newer sklearn versions)
- converts transformed arrays into DataFrames with correct column names
- returns exactly the keys expected by 03_modeling.py:
  features_train, target_train, features_test, target_test, feature_names, preprocessor
"""
from pathlib import Path
from typing import Optional, Dict, List, Any
import warnings

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from scipy import sparse

# -------------------------
# Helper: OneHotEncoder compatibility
# -------------------------
def make_onehot_encoder(**kwargs) -> OneHotEncoder:
    """
    Create OneHotEncoder while handling sklearn version differences:
    - newer versions: OneHotEncoder(sparse_output=False)
    - older versions: OneHotEncoder(sparse=False)
    If neither is accepted, create without dense flag and handle .toarray() later.
    """
    try:
        # prefer new name
        return OneHotEncoder(sparse_output=False, handle_unknown="ignore", **kwargs)
    except TypeError:
        try:
            # older name
            return OneHotEncoder(sparse=False, handle_unknown="ignore", **kwargs)
        except TypeError:
            # last resort: create without dense arg
            warnings.warn(
                "OneHotEncoder: neither 'sparse_output' nor 'sparse' argument is accepted by this sklearn version. "
                "Will encode and convert output to dense using .toarray() when needed."
            )
            return OneHotEncoder(handle_unknown="ignore", **kwargs)

# -------------------------
# Helper: extract feature names from fitted ColumnTransformer
# -------------------------
def _get_feature_names_from_column_transformer(ct: ColumnTransformer, input_features: List[str]) -> List[str]:
    """
    Extract feature names from a fitted ColumnTransformer.
    Works for pipelines with a final estimator that supports get_feature_names_out,
    and handles OneHotEncoder (categories_) fallback.
    """
    feature_names: List[str] = []

    # ct.transformers_ is list of (name, transformer, columns)
    for name, transformer, cols in ct.transformers_:
        if transformer == "drop" or transformer is None:
            continue

        if transformer == "passthrough":
            # passthrough columns keep names
            if isinstance(cols, slice):
                feature_names.extend(input_features[cols])
            else:
                feature_names.extend(list(cols))
            continue

        # If transformer is a Pipeline, take the last step for name extraction
        if hasattr(transformer, "named_steps"):
            trans = transformer.named_steps[list(transformer.named_steps.keys())[-1]]
        else:
            trans = transformer

        # If transformer supports get_feature_names_out, use it
        try:
            if hasattr(trans, "get_feature_names_out"):
                try:
                    # many implementations accept the input column names
                    names = list(trans.get_feature_names_out(cols))
                except Exception:
                    # fallback: call without cols
                    names = list(trans.get_feature_names_out())
                feature_names.extend(names)
                continue
        except Exception:
            pass

        # Fallback for OneHotEncoder older versions
        if trans.__class__.__name__ == "OneHotEncoder":
            try:
                categories = trans.categories_
                for col, cats in zip(cols, categories):
                    col_base = col if isinstance(col, str) else input_features[col]
                    for cat in cats:
                        feature_names.append(f"{col_base}__{cat}")
                continue
            except Exception:
                pass

        # Last fallback: use original column names (may be ambiguous)
        if isinstance(cols, slice):
            feature_names.extend(input_features[cols])
        else:
            feature_names.extend(list(cols))

    return feature_names

# -------------------------
# Core functions
# -------------------------
def load_raw_data(csv_path: Optional[str] = None) -> pd.DataFrame:
    """
    Load raw CSV into a DataFrame. If csv_path is None, use a sensible default.
    Raises FileNotFoundError if not found.
    """
    default_path = Path(
        r"C:\Users\Eyyub\Desktop\StackFuel\PortfolioProjekt\DPP-Stackfuel-Data-Science-Projekt"
        r"\data\raw\diabetes-health-indicators-dataset\diabetes_binary_health_indicators_BRFSS2015.csv"
    )
    p = Path(csv_path) if csv_path else default_path
    p = p.expanduser().resolve(strict=False)
    if not p.exists():
        raise FileNotFoundError(f"CSV file not found at: {p}\nPass csv_path to get_preprocessed_data(csv_path)")
    df = pd.read_csv(p)
    return df

def preprocess_data(
    df: pd.DataFrame,
    target_col: str = "Diabetes_binary",
    test_size: float = 0.2,
    random_state: int = 42
) -> Dict[str, Any]:
    """
    Preprocess DataFrame and return train/test splits plus feature names and preprocessor.
    """
    if target_col not in df.columns:
        raise KeyError(f"Target column '{target_col}' not found. Available columns: {list(df.columns)}")

    target = df[target_col].copy()
    features = df.drop(columns=[target_col]).copy()

    # Identify numeric and categorical columns (heuristics)
    numeric_cols = features.select_dtypes(include=["number"]).columns.tolist()
    object_cols = features.select_dtypes(include=["object", "category"]).columns.tolist()

    # Treat low-cardinality numeric columns as categorical
    low_cardinality = [c for c in numeric_cols if features[c].nunique() <= 10]
    numeric_cols = [c for c in numeric_cols if c not in low_cardinality]
    categorical_cols = object_cols + low_cardinality

    # Build pipelines
    numeric_pipeline = Pipeline([("scaler", StandardScaler())])
    ohe = make_onehot_encoder()
    categorical_pipeline = Pipeline([("ohe", ohe)])

    transformers = []
    if numeric_cols:
        transformers.append(("num", numeric_pipeline, numeric_cols))
    if categorical_cols:
        transformers.append(("cat", categorical_pipeline, categorical_cols))

    preprocessor = ColumnTransformer(transformers=transformers, remainder="drop")

    # Train-test split before fitting preprocessor to avoid leakage
    features_train_raw, features_test_raw, target_train, target_test = train_test_split(
        features, target, test_size=test_size, stratify=target, random_state=random_state
    )

    # Fit preprocessor on training raw data
    preprocessor.fit(features_train_raw)

    # Transform (result may be sparse matrix or numpy array)
    features_train_trans = preprocessor.transform(features_train_raw)
    features_test_trans = preprocessor.transform(features_test_raw)

    # If sparse, convert to dense
    if sparse.issparse(features_train_trans):
        features_train_trans = features_train_trans.toarray() # pyright: ignore[reportAttributeAccessIssue]
    if sparse.issparse(features_test_trans):
        features_test_trans = features_test_trans.toarray() # pyright: ignore[reportAttributeAccessIssue]

    # Ensure numpy array
    features_train_trans = np.asarray(features_train_trans)
    features_test_trans = np.asarray(features_test_trans)

    # Get feature names (with fallback)
    input_features = list(features.columns)
    try:
        feature_names = _get_feature_names_from_column_transformer(preprocessor, input_features)
    except Exception as e:
        warnings.warn(f"Could not extract feature names from ColumnTransformer: {e}. Using generic names.")
        feature_names = [f"feature_{i}" for i in range(features_train_trans.shape[1])]

    # If length mismatch between names and transformed columns, fallback to generic names
    if len(feature_names) != features_train_trans.shape[1]:
        warnings.warn(
            f"Mismatch between extracted feature name count ({len(feature_names)}) "
            f"and transformed array width ({features_train_trans.shape[1]}). Falling back to generic names."
        )
        feature_names = [f"feature_{i}" for i in range(features_train_trans.shape[1])]

    # Convert transformed arrays to DataFrames so .columns exist downstream
    features_train_df = pd.DataFrame(features_train_trans, columns=feature_names, index=features_train_raw.index)
    features_test_df = pd.DataFrame(features_test_trans, columns=feature_names, index=features_test_raw.index)

    return {
        "features_train": features_train_df,
        "features_test": features_test_df,
        "target_train": target_train,
        "target_test": target_test,
        "feature_names": feature_names,
        "preprocessor": preprocessor,
    }

def get_preprocessed_data(csv_path: Optional[str] = None) -> Dict[str, Any]:
    """
    Convenience wrapper: load raw csv_path and return output of preprocess_data.
    """
    df = load_raw_data(csv_path)
    return preprocess_data(df)

# -------------------------
# Quick CLI test
# -------------------------
if __name__ == "__main__":
    try:
        out = get_preprocessed_data()
        print("Preprocessing complete.")
        print(f"Train samples: {len(out['features_train'])}, Test samples: {len(out['features_test'])}")
        print(f"Transformed feature count: {len(out['feature_names'])}")
        print("First 20 transformed feature names:", out["feature_names"][:20])
    except Exception as e:
        print("Error in preprocessing:", e)