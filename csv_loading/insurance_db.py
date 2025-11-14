import sqlite3
import pandas as pd

def save_to_sqlite(df, table_name="insurance", db_file="insuarance_data.db"):
    """
    Save a pandas DataFrame to SQLite database
    
    df: Your cleaned DataFrame
    table_name: What to call the table in database  
    db_file: The SQLite file name
    """
    # Connect to database (creates file if doesn't exist)
    conn = sqlite3.connect(db_file)
    
    # Save DataFrame to SQLite table
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    # Close connection
    conn.close()
    
    print(f"✅ Saved {len(df)} rows to '{table_name}' in {db_file}")



