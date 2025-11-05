import pandas as pd
from db import create_tables, add_user

def main():
    create_tables()
    add_user("Chacha", "chacha@example.com")

if __name__ == "__main__":
    main()

#%%