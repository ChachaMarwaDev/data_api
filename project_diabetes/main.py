# We join all the information
from src.extract import extract_csv
from src.transform import clean_data
# from src.load import load_data

def main():
    try:
        raw_data = extract_csv("diabetes_012_health_indicators_BRFSS2015.csv") 
    except FileNotFoundError:
        print("ERROR: CSV file not found. Please verify the filename and location")
        return

    cleaned = clean_data(raw_data)

    print(f"Rows before cleaning: {len(raw_data)}")
    print(f"Rows after cleaning: {len(cleaned)}")

    cleaned.to_csv("cleaned_diabetes02.csv", index=False)
    print("clean data exported")

    # load_data(cleaned, "diabetes_cleaned.csv")
    return cleaned

if __name__ == "__main__":
    cleaned_df = main()

# clean_data()