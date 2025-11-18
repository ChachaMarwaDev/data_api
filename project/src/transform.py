# Data processing will take place
# from src.extract import df #this causes an error
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Inspect
    print(df.head(5))
    return df
