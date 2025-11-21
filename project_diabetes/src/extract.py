# File will entail path configuration
from src.config import DATA_DIR # file path variable in the config.py that makes it easier to deal
import pandas as pd

def extract_csv(filename: str) -> pd.DataFrame: # a function giving a filename into string and once done it gives back the pandas dataframe
    file_path = DATA_DIR / filename # the / operator lets us add neatly the filename at the end of the DATA_PATH
    print("Loading:", file_path.resolve()) #shows the path loaded on the terminal

    df = pd.read_csv(file_path) #takes the path as it is and does not accept file path

    return df