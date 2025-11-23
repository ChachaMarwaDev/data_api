# Data processing will take place
# from src.extract import df #this causes an error
import pandas as pd
import matplotlib.pyplot as plt

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
    # print(df.nunique()) # we have categorical ['Diabetes_012', 'HighBP', 'HighChol', 'CholCheck', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'DiffWalk', 'Sex'] and numerical data ['BMI', 'MentHlth', 'PhysHlth', 'Age', 'Education', 'Income']
   #  print("Before deleting" ,df.duplicated().sum()) # we have 23899 duplicate values 
   #  print("Sex description: ", df['Sex'].describe())
   #  df.drop_duplicates(inplace=True)

   #  remake of the columns to int
    df[['Age', 'Diabetes_012', 'HighBP', 'HighChol', 'CholCheck', 'Smoker']] = df[['Age', 'Diabetes_012', 'HighBP', 'HighChol', 'CholCheck', 'Smoker']].astype(int)

   # # remake the sex column to meaning
    df['Sex'] = df['Sex'].map({1 :'Male', 0 : 'Female'})
    df['Smoker'] = df['Smoker'].map({1 :'Yes', 0 : 'No'})
   #  print(df['Smoker'].head(5))
   # #  print(df['Sex'].tail(5))
   #  print("The count of Smoker :", df['Smoker'].describe())

   # print()
    df.rename(columns={'Diabetes_012' : 'Diab_Condi'}, inplace=True)

   #  age_mapping = {
   #      1:'18-24', 2: '25-29', 3: '30-34', 4: '35-39', 5: '40-44', 6: '45-49', 7: '50-54', 8: '55-59',  9: '60-64', 10: '65-69', 11: '70-74', 12: '75-79', 13: '80+'
   #  }
   #  df['AgeGroup'] = df['Age'].map(age_mapping)
   #  diabetes_rate = df.groupby(['AgeGroup', 'Sex'])['Diab_Condi'].mean()
   #  diabetes_rate.plot(kind='bar')
   #  plt.title('Gender differences in diabetes rates across different age groups')
   #  plt.show()

    activity_smoke_risk = df.groupby(['Smoker', 'PhysActivity'])['Diab_Condi'].mean()

    print(activity_smoke_risk)

    activity_smoke_risk.plot(kind='bar')
    plt.title('Diabetes rates by Smoking & Physical Activity')
    plt.ylabel('Avg Diabetes Rate')
    plt.show()

   #  risk_stats = df.groupby(['HighBP', 'HighChol'])['Diab_Condi'].agg(['mean', 'count'])
   #  print(risk_stats)

   #  risk_stats['mean'].plot(kind='bar')
   #  plt.title('Average diabetes rate by blood pressure and cholesterol combination') 
   #  plt.ylabel('Diabetes Rate(mean)') # 0,0 = none; 0,1 = cholestrolOnly; 1,0 = bloodpressureOnly; 1,1 = both;
   #  plt.show()

   # questions for drawing insights
   #  df.groupby('Age')['Diab_Condi'].mean().plot.bar()
   #  plt.title('Age groups having the highest diabetes prevalence')
   #  plt.xlabel('Age')
   #  plt.ylabel('Diabetes condition')
   #  plt.show()

   #  df.groupby('Income')['Diab_Condi'].mean().plot.bar()
   #  plt.title('Income level correlating with diabetes risk')
   #  plt.xlabel('Income')
   #  plt.ylabel('Diabetes condition')
   #  plt.show()

    return df
