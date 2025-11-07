import pandas as pd
from pathlib import Path
# from db import create_tables, add_user

# def main():
#     create_tables()
#     add_user("Chacha", "chacha@example.com")

# if __name__ == "__main__":
#     main()
path = Path(r"csv_files\insurance.csv")
df = pd.read_csv(path)

#shows column names in dataframe
# print(df.columns)

# gives a statistical summary of numerical columns
# print(df.info()) 


# print(df.describe())
