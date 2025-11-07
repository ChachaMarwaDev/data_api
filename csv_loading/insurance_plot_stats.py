from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Loading the csv file 
path = Path(r"csv_files\insurance.csv")
df = pd.read_csv(path)


#columns name:['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
mean_value = df['children'].mean()
median_value = df['children'].median()
mode_value = df['children'].mode()[0]  # [0] gets the first mode if there are multiple

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)


# Plot histogram to show distribution
plt.figure(figsize=(8,5))
plt.hist(df['children'], bins=10, color='lightblue', edgecolor='black')

# Plot vertical lines for mean, median, mode
plt.axvline(mean_value, color='red', linestyle='--', label=f'Mean: {mean_value:.2f}')
plt.axvline(median_value, color='green', linestyle='--', label=f'Median: {median_value:.2f}')
plt.axvline(mode_value, color='orange', linestyle='--', label=f'Mode: {mode_value:.2f}')

# Add title and legend
plt.title('Mean, Median, and Mode Visualization on bmi')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.legend()

# Show the plot
plt.show()