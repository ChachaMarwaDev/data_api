# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the input DataFrame by performing data type conversions, value mappings,
    and column renaming. This function assumes the DataFrame contains health-related
    survey data with columns like 'Diabetes_012', 'HighBP', etc.

    Args:
        df (pd.DataFrame): The raw DataFrame to be cleaned.

    Returns:
        pd.DataFrame: The cleaned DataFrame with updated data types and mappings.
    """
    
    # Section 1: Data Inspection (Commented out for production; used during development)
    # Uncomment these lines to inspect the data structure, null values, duplicates, etc.
    # print(df.head(5))  # Display first 5 rows
    # print(df.dtypes)   # Check data types (all rows have float values initially)
    # print(df.columns)  # List all columns
    # Expected columns: ['Diabetes_012', 'HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker',
    #                    'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
    #                    'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
    #                    'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']
    # print(df.isnull().sum())  # Check for null values (0 nulls expected)
    # print(df.nunique())       # Check unique values per column
    # Categorical columns: ['Diabetes_012', 'HighBP', 'HighChol', 'CholCheck', 'Smoker', 'Stroke',
    #                       'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
    #                       'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'DiffWalk', 'Sex']
    # Numerical columns: ['BMI', 'MentHlth', 'PhysHlth', 'Age', 'Education', 'Income']
    # print("Before deleting duplicates:", df.duplicated().sum())  # Count duplicates (e.g., 23899)
    # print("Sex description:", df['Sex'].describe())
    
    # Section 2: Data Cleaning Operations
    
    # Remove duplicate rows to ensure data integrity
    df.drop_duplicates(inplace=True)
    
    # Convert specified columns to integer type for consistency
    # These columns represent categorical or ordinal data that should be integers
    df[['Age', 'Diabetes_012', 'HighBP', 'HighChol', 'CholCheck', 'Smoker']] = \
        df[['Age', 'Diabetes_012', 'HighBP', 'HighChol', 'CholCheck', 'Smoker']].astype(int)
    
    # Map numerical values to descriptive strings for better readability
    # Sex: 1 -> 'Male', 0 -> 'Female'
    df['Sex'] = df['Sex'].map({1: 'Male', 0: 'Female'})
    
    # Smoker: 1 -> 'Yes', 0 -> 'No'
    df['Smoker'] = df['Smoker'].map({1: 'Yes', 0: 'No'})
    
    # Rename column for clarity (Diabetes_012 -> Diab_Condi)
    df.rename(columns={'Diabetes_012': 'Diab_Condi'}, inplace=True)
    
    # Section 3: Exploratory Analysis (Commented out; examples for visualization and insights)
    # Uncomment and modify these sections to perform analysis during development.
    # Note: These require matplotlib and may need adjustments based on data.
    
    # Example: Age group mapping and diabetes rate by age and sex
    # age_mapping = {
    #     1: '18-24', 2: '25-29', 3: '30-34', 4: '35-39', 5: '40-44',
    #     6: '45-49', 7: '50-54', 8: '55-59', 9: '60-64', 10: '65-69',
    #     11: '70-74', 12: '75-79', 13: '80+'
    # }
    # df['AgeGroup'] = df['Age'].map(age_mapping)
    # diabetes_rate = df.groupby(['AgeGroup', 'Sex'])['Diab_Condi'].mean()
    # diabetes_rate.plot(kind='bar')
    # plt.title('Gender differences in diabetes rates across different age groups')
    # plt.show()
    
    # Example: Diabetes rates by smoking and physical activity
    # activity_smoke_risk = df.groupby(['Smoker', 'PhysActivity'])['Diab_Condi'].mean()
    # print(activity_smoke_risk)
    # activity_smoke_risk.plot(kind='bar')
    # plt.title('Diabetes rates by Smoking & Physical Activity')
    # plt.ylabel('Avg Diabetes Rate')
    # plt.show()
    
    # Example: Diabetes rates by high blood pressure and high cholesterol
    # risk_stats = df.groupby(['HighBP', 'HighChol'])['Diab_Condi'].agg(['mean', 'count'])
    # print(risk_stats)
    # risk_stats['mean'].plot(kind='bar')
    # plt.title('Average diabetes rate by blood pressure and cholesterol combination')
    # plt.ylabel('Diabetes Rate (mean)')  # 0,0 = none; 0,1 = cholesterol only; 1,0 = blood pressure only; 1,1 = both
    # plt.show()
    
    # Example: Diabetes prevalence by age group
    # df.groupby('Age')['Diab_Condi'].mean().plot.bar()
    # plt.title('Age groups having the highest diabetes prevalence')
    # plt.xlabel('Age')
    # plt.ylabel('Diabetes condition')
    # plt.show()
    
    # Example: Diabetes risk by income level
    # df.groupby('Income')['Diab_Condi'].mean().plot.bar()
    # plt.title('Income level correlating with diabetes risk')
    # plt.xlabel('Income')
    # plt.ylabel('Diabetes condition')
    # plt.show()
    
    # Return the cleaned DataFrame
    return df
