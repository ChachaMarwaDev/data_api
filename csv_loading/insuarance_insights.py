from pathlib import Path
import pandas as pd

# Loading the csv file 
path = Path(r"csv_processed_files\insurance_procesessed.csv")
df = pd.read_csv(path)

# 🗺️ Which region has many smokers and vice versa?
# region_smoker = df.groupby('region')['smoker'].value_counts(normalize=True)
# print('No. of smokers per region:\n', region_smoker)
# 🚬 What sex has high % of smokers and vice versa?
# sex_smoke = pd.crosstab(df['sex'], df['smoker'], normalize='index')
# print('High % of smokers from each sex:\n', sex_smoke)
# 👥 Which sex dominates in each region?
# region_sex = df.groupby('region')['sex'].value_counts(normalize=True)
# print('Sex dominating each region\n', region_sex)
# 💰 What age incurs a high charge?
# age_charges = df.groupby('charges')['age'].mean()
# print(age_charges)
# 👶 Does having children increase the charges?
# children_charges = df.groupby('children')['charges'].mean()
# print('children increases charges', children_charges)
# 🧒 Which age gap has children?
# pd.cut(df['age'], bins=[18,25,35,45,55,65,80]).value_counts()
# 🧾 Does having many children in a region increase charges?
# df.groupby(['region','children'])['charges'].mean()
# 🌍 What region pays high charges and vice versa?
# df.groupby('region')['charges'].mean().sort_values(ascending=False)
# 📊 What age dominates in each region?
# df.groupby('region')['age'].mean() or mode()

