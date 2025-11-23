# **ETL Practice Project – Insurance Dataset**

This project marks the beginning of my journey into data engineering. I wanted to understand the full ETL (Extract, Transform, Load) process using simple CSV files before moving into larger systems. I collected datasets from platforms such as HuggingFace and Kaggle, starting with **insurance.csv**, as it offers rich features to practice cleaning, analysis, and storage.

---

## **ETL Workflow I Followed**

### **1. Extract**

* Downloaded datasets from public sources.
* Loaded the CSV into Python using `pandas.read_csv()`.

### **2. Inspect**

* Reviewed the structure of the DataFrame.
* Checked column types, missing values, and inconsistencies.
* Looked for unrealistic values and potential outliers (example: unusually high number of children).

### **3. Clean**

* Removed or corrected incorrect values.
* Standardized column formats.
* Used functions to automate repeated cleaning steps.
* Practiced writing clear, reusable Python functions.

### **4. Explore**

* Performed descriptive analysis.
* Examined relationships between variables (e.g., age vs. charges, smoker status vs. region).
* Identified patterns and anomalies worth investigating further.

### **5. Transform**

* Converted cleaned data into a more structured format.
* Applied feature adjustments and prepared it for storage.
* Practiced writing transformation logic without hard-coding paths by using relative paths and raw strings (`r""`).

### **6. Load**

* Stored the transformed data in an SQLite database.
* Created a Python configuration file to manage database connections.
* Used SQL queries to verify tables and answer analysis questions.

---

## **What I Learned**

* **Core Pandas operations** such as `read_csv`, `to_csv`, basic cleaning, filtering, and column manipulation.
* **Better Python habits**, including writing simple functions to avoid repetition.
* **Using relative paths** properly so scripts work across environments without hard-coded absolute paths.
* **Storing data in SQLite** and interacting with it using SQL and Python.

---

## **Challenges I Faced**

* Turning raw observations into **meaningful analysis**.
* Knowing what to remove, what to keep, and how to treat outliers.
* Plotting data clearly and choosing the right visualizations.
* Interpreting results instead of just printing them.
* Maintaining clarity when shifting between Python, Pandas, and SQL.

---

## **My Journey So Far**

Working with the insurance dataset felt like a cycle of discovery:

* **Extraction** was smooth and exciting — loading the CSV gave me momentum.
* **Transformation** pushed me to slow down and think more carefully.
* **Database loading** challenged me the most; learning to set up configuration files and interact with SQLite was a turning point.
* My SQL skills helped anchor the final phase, where I used queries to verify and analyze the cleaned data.

There were moments of excitement, confusion, stress, and relief — but they led to confidence and clarity. This is the cycle I expect to repeat as I continue sharpening my weak areas and building stronger foundations in data engineering.

---

## **Next Steps**

* Reinforce concepts I struggled with, especially data analysis and visualization.
* Explore more datasets and repeat the ETL workflow until it becomes second nature.
* Gradually move from CSV files to larger, real-world data pipelines.
* Build small tools or scripts that automate parts of the ETL process.

