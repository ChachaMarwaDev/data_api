import sqlite3


try:
    # Connect to SQLite Database and create a cursor
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')
    
    # Close the cursor after use
    cursor.close()

except sqlite3.Error as error:
    print('Error occurred -', error)

finally:
    # Ensure the database connection is closed
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')