# File will entail path configuration
import pandas as pd
from pathlib import Path
from src.config import DATA_PATH # file path variable in the config.py that makes it easier to deal

def extract_csv(filename: str) -> pd.DataFrame: # a function giving a filename into string and once done it gives back the pandas dataframe
    file_path = Path(DATA_PATH) / filename # the / operator lets us add neatly the filename at the end of the DATA_PATH
    df = pd.read_csv(file_path)
    return df