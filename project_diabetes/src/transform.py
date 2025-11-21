# Data processing will take place
# from src.extract import df #this causes an error
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Inspect
    # print(df.head(5))
    # print(df.dtypes) # All rows have float values
    # print(df.columns)
    '''['Diabetes_012', 'HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker',
       'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
       'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
       'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education',
       'Income']'''

    # print(df.isnull().sum()) # we have 0 null values
    # print(df.nunique()) # we have categorical ['Diabetes_012', 'HighBP', 'HighChol', 'CholCheck', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'DiffWalk', 'Sex'] and non-categorical data ['BMI', 'MentHlth', 'PhysHlth', 'Age', 'Education', 'Income']
   #  print("Before deleting" ,df.duplicated().sum()) # we have 23899 duplicate values 
   #  print("Sex description: ", df['Sex'].describe())
   #  df.drop_duplicates(inplace=True)

   # # remake the sex column to meaning
   #  df['Sex'] = df['Sex'].map({1 :'Male', 0 : 'Female'})
   # #  print(df['Sex'].head(5))
   # #  print(df['Sex'].tail(5))
   #  print("The count of sex :", df['Sex'].describe())

   #  remake of the columns to int
    df[['Age', 'Diabetes_012', 'HighBP', 'HighChol', 'CholCheck', 'Smoker']] = df[['Age', 'Diabetes_012', 'HighBP', 'HighChol', 'CholCheck', 'Smoker']].astype(int)

   #  print()

    return df
