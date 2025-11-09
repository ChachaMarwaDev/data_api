import pandas as pd
from pathlib import Path
import seaborn as sns
# from db import create_tables, add_user

# def main():
#     create_tables()
#     add_user("Chacha", "chacha@example.com")

# if __name__ == "__main__":
#     main()

# Data loading
# path = Path(r"csv_raw_files\insurance.csv")
# df = pd.read_csv(path)
# # making a temporary copy of the file
# df_copy = df.copy()


path = Path(r"csv_processed_files\insurance_procesessed.csv")
df = pd.read_csv(path)

print(df['age'].corr(df['bmi']))
# print(pd.crosstab(df['smoker'], df['sex']))


#Data inspection

#shows column names in dataframe
# print(df.columns) # these are columns:['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']

# checking the data types 
# print(df_copy.dtypes)
# gives a statistical summary of numerical columns
# print(df_copy.info()) 

# see statistical summary
# print(df_copy.describe())

# Checks a no. of missing values in each column
# print(df_copy.isnull().sum()) # columns age,bmi,children have 1 missing value

# check for duplicate rows
# print(df_copy.duplicated().sum()) # there is 1 duplicate row

# check no. of unique values
# print(df_copy.nunique()) # age:47, sex:2, bmi:548, children:6, smoker:2, region:4, charges:1337

# Filling data
# df_copy.fillna(df_copy['age'].median(), inplace=True)
# df_copy.fillna(df_copy['bmi'].median(), inplace=True)
# df_copy.fillna(df_copy['children'].median(), inplace=True)

# Changing data types
# df_copy['children'] = df_copy['children'].astype(int)
# df_copy['age'] = df_copy['age'].astype(int)
# print(df_copy['children'].head(5))

# print(df_copy.head(5))
# print(df_copy.tail(5))
# print(df_copy.info())

# df_copy = df_copy.round(2)

# df_copy.to_csv("csv_processed_files/insurance_procesessed.csv", float_format="%.2f", index=False)
# print('done')


'''
do we do the same using the raw string when saving?
'''