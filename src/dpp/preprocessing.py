import os
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_raw_data(csv_path: str | None = None) -> pd.DataFrame:
    """
    Load raw data from a CSV file.

    Parameters
    ----------
    csv_path : str | None
        Path to the CSV file. If None, a sensible default path will be used
        (adjusted for the user's project layout). The function will expand
        user (~) paths and resolve relative paths.

    Returns
    -------
    pd.DataFrame
        Loaded raw data.

    Raises
    ------
    FileNotFoundError
        If the CSV file cannot be found at the resolved path.
    """
    # Default path (use the absolute path you provided)
    default_path = Path(
        r"C:\Users\Eyyub\Desktop\StackFuel\PortfolioProjekt\DPP-Stackfuel-Data-Science-Projekt"
        r"\data\raw\diabetes-health-indicators-dataset\diabetes_binary_health_indicators_BRFSS2015.csv"
    )

    if csv_path is None:
        csv_path = default_path # pyright: ignore[reportAssignmentType]
    else:
        csv_path = Path(csv_path) # pyright: ignore[reportAssignmentType]

    # Expand and resolve path to an absolute path
    csv_path = csv_path.expanduser() # pyright: ignore[reportAttributeAccessIssue, reportOptionalMemberAccess]
    try:
        csv_path = csv_path.resolve(strict=False) # pyright: ignore[reportOptionalMemberAccess, reportAttributeAccessIssue]
    except Exception:
        # resolve(strict=False) is used to avoid raising if intermediate parts are missing;
        # we'll check existence below and raise a clearer FileNotFoundError.
        pass

    if not csv_path.exists(): # pyright: ignore[reportOptionalMemberAccess, reportAttributeAccessIssue]
        raise FileNotFoundError(f"CSV file not found at: {csv_path}\n"
                                "Please verify the path or pass csv_path explicitly to get_preprocessed_data(csv_path).")

    # Read CSV into DataFrame
    df = pd.read_csv(csv_path) # pyright: ignore[reportArgumentType]
    return df


def preprocess_data(df: pd.DataFrame) -> dict:
    """
    Preprocess raw data: separate features and target, scale numeric features,
    split into train/test sets, and return data with original feature names.

    This function is intentionally simple: it does not perform one-hot encoding.
    If your pipeline uses encoding or column expansion, adapt this function to
    also return post-transformation feature names (e.g. from OneHotEncoder.get_feature_names_out()).

    Parameters
    ----------
    df : pd.DataFrame
        Raw input data.

    Returns
    -------
    dict
        Dictionary with:
            - 'X_train', 'X_test' : pd.DataFrame (scaled)
            - 'y_train', 'y_test' : pd.Series
            - 'feature_names'      : list[str] original feature names (before encoding)
    """
    # Ensure expected target column exists
    target_col = 'Diabetes_binary'
    if target_col not in df.columns:
        raise KeyError(f"Target column '{target_col}' not found in dataframe. Available columns: {list(df.columns)}")

    # Separate target and predictors
    target = df[target_col].copy()
    features = df.drop(columns=[target_col]).copy()

    # Save original feature names (pre-transformation)
    feature_names = list(features.columns)

    # Simple numeric scaling (keeps as DataFrame to retain column names)
    scaler = StandardScaler()
    features_scaled_array = scaler.fit_transform(features)
    features_scaled = pd.DataFrame(features_scaled_array, columns=feature_names, index=features.index)

    # Train-test split with stratification on the target
    features_train, features_test, target_train, target_test = train_test_split(
        features_scaled, target, test_size=0.2, random_state=42, stratify=target
    )

    return {
        'features_train': features_train,
        'features_test': features_test,
        'target_train': target_train,
        'target_test': target_test,
        'feature_names': feature_names
    }


def get_preprocessed_data(csv_path: str | None = None) -> dict:
    """
    Convenience wrapper: load raw data and return preprocessed datasets and feature names.

    Parameters
    ----------
    csv_path : str | None
        Optional custom path to the CSV file. If None, the hard-coded project path
        (provided by the user) will be used as default.

    Returns
    -------
    dict
        Output of preprocess_data containing preprocessed train/test splits and feature names.
    """
    df = load_raw_data(csv_path)
    return preprocess_data(df)


if __name__ == "__main__":
    # Example usage: call with no arguments to use the default path,
    # or pass csv_path=r"C:\path\to\file.csv"
    try:
        data = get_preprocessed_data()  # or get_preprocessed_data(csv_path="C:/...")
        print("Preprocessing complete. Data ready for modeling.")
        print(f"Training samples: {len(data['X_train'])}")
        print(f"Test samples: {len(data['X_test'])}")
        print(f"Number of features: {len(data['feature_names'])}")
        print("Feature names:")
        print(data['feature_names'])
    except Exception as e:
        # Provide a friendly error message
        print("Error during preprocessing:", e)
        print("If the file exists elsewhere, call get_preprocessed_data(csv_path='full/path/to/file.csv')")