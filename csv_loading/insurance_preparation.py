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

print(df.columns)

print(df['age'])
# know the types of data in our csv file
# dataTypes = print(df.dtypes)

# First5 = df.head(5)
# print(First5)

# last5 = df.tail(5)
# print(last5)

# print(df.columns)
# 'age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'
'''
how do we select a one column?
how do we select two columns?
'''

