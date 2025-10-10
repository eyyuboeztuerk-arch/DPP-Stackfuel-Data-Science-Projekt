# src/dpp/preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
import warnings

warnings.filterwarnings('ignore')

def load_raw_data(csv_path: str = 'data/raw/diabetes_binary_health_indicators_BRFSS2015.csv') -> pd.DataFrame:
    """
    Load the raw dataset from a CSV file.
    
    This function reads the diabetes health indicators dataset from a CSV file
    and returns it as a pandas DataFrame.
    
    Parameters:
    -----------
    csv_path : str, optional
        Path to the CSV file containing the raw data.
        Default is 'data/raw/diabetes_binary_health_indicators_BRFSS2015.csv'
        
    Returns:
    --------
    pd.DataFrame
        DataFrame containing the raw dataset with all features and target variable.
    """
    df = pd.read_csv(csv_path)
    return df

def create_preprocessing_pipeline():
    """
    Create preprocessing pipelines for different feature groups.
    
    This function defines and combines multiple preprocessing pipelines for:
    - Continuous features: Median imputation + Robust scaling
    - Ordinal features: Most frequent imputation + Standard scaling
    - Binary health features: Most frequent imputation (no scaling)
    - Demographic features: Most frequent imputation (no scaling)
    
    The pipelines are combined using ColumnTransformer to handle different
    feature types appropriately.
    
    Returns:
    --------
    sklearn.compose.ColumnTransformer
        A fitted ColumnTransformer object that can be used to preprocess the data.
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