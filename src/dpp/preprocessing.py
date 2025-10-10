# src/dpp/preprocessing.py

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
import warnings

warnings.filterwarnings('ignore')


def load_raw_data(csv_path: str | None = None) -> pd.DataFrame:
    """
    Load the raw dataset from a CSV file.

    The function will use the provided `csv_path` if given. If not provided,
    it will build a default path relative to the project root:

      <project_root>/data/raw/diabetes-health-indicators-dataset/diabetes_binary_health_indicators_BRFSS2015.csv

    Parameters
    ----------
    csv_path : str | None, optional
        Full path to the CSV file. If None, the function builds a default
        path relative to this file's location.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the raw dataset.

    Raises
    ------
    FileNotFoundError
        If the CSV file cannot be found at the resolved path.
    """
    if csv_path is None:
        # Resolve project root from this file location:
        # project_root/
        #   src/
        #     dpp/
        #       preprocessing.py  <-- this file
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        csv_path = os.path.join(
            base_dir,
            'data',
            'raw',
            'diabetes-health-indicators-dataset',
            'diabetes_binary_health_indicators_BRFSS2015.csv'
        )

    csv_path = os.path.abspath(csv_path)
    print(f"[preprocessing] Loading data from: {csv_path}")

    if not os.path.exists(csv_path):
        raise FileNotFoundError(
            f"CSV file not found at: {csv_path}\n"
            "Please verify the path or call get_preprocessed_data(csv_path='YOUR_PATH')"
        )

    df = pd.read_csv(csv_path)
    return df


def create_preprocessing_pipeline():
    """
    Create preprocessing pipelines for different feature groups.

    Returns
    -------
    sklearn.compose.ColumnTransformer
        A ColumnTransformer that handles continuous, ordinal, binary health
        and demographic features.
    """
    binary_health = ['HighBP', 'HighChol', 'CholCheck', 'Smoker', 'Stroke',
                     'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
                     'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'DiffWalk']
    ordinal = ['GenHlth', 'Age', 'Education', 'Income']
    continuous = ['BMI', 'MentHlth', 'PhysHlth']
    demographic = ['Sex', 'Age', 'Education', 'Income']

    continuous_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', RobustScaler())
    ])

    ordinal_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('scaler', StandardScaler())
    ])

    binary_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent'))
    ])

    demographic_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent'))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ('cont', continuous_transformer, continuous),
        ('ord', ordinal_transformer, ordinal),
        ('bin', binary_transformer, binary_health),
        ('demo', demographic_transformer, demographic)
    ], remainder='drop')

    return preprocessor


def preprocess_data(df: pd.DataFrame, target_col: str = 'Diabetes_binary', test_size=0.2, random_state=42):
    """
    Perform complete preprocessing and return train/test data.

    Steps:
      - drop duplicates
      - separate X and y
      - build preprocessing pipeline
      - train/test split with stratification
      - fit/transform pipeline on train and transform test
      - apply SMOTE to training set to handle class imbalance

    Returns a dict with keys: 'preprocessor', 'features_train', 'target_train', 'features_test', 'target_test'.
    """
    # remove duplicates
    df = df.drop_duplicates()

    # split target and features
    if target_col not in df.columns:
        raise KeyError(f"Target column '{target_col}' not found in dataframe columns.")

    target = df[target_col]
    features = df.drop(columns=[target_col])

    preprocessor = create_preprocessing_pipeline()

    features_train, features_test, target_train, target_test = train_test_split(
        features, target, test_size=test_size, random_state=random_state, stratify=target
    )

    features_train_processed = preprocessor.fit_transform(features_train)
    features_test_processed = preprocessor.transform(features_test)

    smote = SMOTE(random_state=random_state)
    features_train_resampled, target_train_resampled = smote.fit_resample(features_train_processed, target_train) # pyright: ignore[reportAssignmentType]

    return {
        'preprocessor': preprocessor,
        'features_train': features_train_resampled,
        'target_train': target_train_resampled,
        'features_test': features_test_processed,
        'target_test': target_test
    }


def get_preprocessed_data(csv_path: str | None = None):
    """
    Convenience function to load raw data and return preprocessed data.

    Parameters
    ----------
    csv_path : str | None, optional
        Path to CSV. If None, default relative path is used (see load_raw_data).

    Returns
    -------
    dict
        Dictionary containing preprocessor, preprocessed train/test data and labels.
    """
    df = load_raw_data(csv_path)
    data = preprocess_data(df)
    return data


if __name__ == "__main__":
    # Example usage: the default resolution should match your provided path.
    try:
        data = get_preprocessed_data()
        print("Preprocessing complete. Data ready for modeling.")
        print(f"Training samples: {len(data['features_train'])}")
        print(f"Test samples: {len(data['features_test'])}")
    except Exception as e:
        print("Error during preprocessing:", e)