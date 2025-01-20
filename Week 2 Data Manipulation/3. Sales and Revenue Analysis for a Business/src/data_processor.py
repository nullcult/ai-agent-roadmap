import pandas as pd

class DataProcessor:
    def load_data(self, file_path):
        """
        Load data from CSV or Excel file
        """
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path, skipinitialspace=True)
        elif file_path.endswith(('.xlsx', '.xls')):
            return pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Please use CSV or Excel files.")
    
    def clean_data(self, df):
        """
        Clean and preprocess the data
        """
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Handle missing values
        df = df.dropna()
        
        # Convert date column to datetime
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
        
        return df
