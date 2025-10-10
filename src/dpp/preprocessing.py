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