# We join all the information
from src.extract import extract_csv
from src.transform import clean_data

def main():
    raw_data = extract_csv("diabetes_012_health_indicators_BRFSS2015.csv")
    cleaned = clean_data(raw_data)

    return cleaned

if __name__ == "__main__":
    cleaned_df = main()

# clean_data()