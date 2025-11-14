import sqlite3

DB_FILE = "insuarance_data.db"

def run_query(query):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# --------------------------------------------
# EXAMPLES
# --------------------------------------------

# Check all tables
# tables = run_query("SELECT name FROM sqlite_master WHERE type='table';")
# print("Tables:", tables)

# # Preview your data
# rows = run_query("SELECT * FROM insurance LIMIT 5;")
# print("Sample rows:", rows)

# print(run_query("SELECT COUNT(*) FROM insurance;"))

# print(run_query("SELECT age, charges " \
#                 "FROM insurance " \
#                 "WHERE age > 50 " \
#                 "ORDER BY age DESC " \
#                 "LIMIT 10 ;"))

print(run_query("SELECT DISTINCT children FROM insurance;"))

'''
age, sex, bmi, smoker, region, charges 
'''
