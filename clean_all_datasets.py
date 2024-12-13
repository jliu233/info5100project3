import pandas as pd

# File paths for the original files
inflation_file_path = "inflationRate.csv"
unemployment_file_path = "unemploymentRate.csv"

# Clean inflation dataset
inflation_data = pd.read_csv(inflation_file_path, skiprows=5)  # Skip the metadata rows
inflation_cleaned = inflation_data.rename(columns={
    inflation_data.columns[0]: "Date",
    inflation_data.columns[1]: "ConsumerPriceIndex"
})[["Date", "ConsumerPriceIndex"]]  # Keep only relevant columns
inflation_cleaned["Date"] = pd.to_datetime(inflation_cleaned["Date"], errors="coerce")
inflation_cleaned = inflation_cleaned.dropna()  # Remove rows with invalid dates or CPI values

# Clean unemployment dataset
unemployment_data = pd.read_csv(unemployment_file_path, skiprows=5)  # Skip the metadata rows
unemployment_cleaned = unemployment_data.rename(columns={
    unemployment_data.columns[0]: "Date",
    unemployment_data.columns[1]: "UnemploymentRate"
})[["Date", "UnemploymentRate"]]  # Keep only relevant columns
unemployment_cleaned["Date"] = pd.to_datetime(unemployment_cleaned["Date"], errors="coerce")
unemployment_cleaned = unemployment_cleaned.dropna()  # Remove rows with invalid dates or rates

# Save cleaned datasets to new files
inflation_cleaned.to_csv("cleaned_inflationRate.csv", index=False)
unemployment_cleaned.to_csv("cleaned_unemploymentRate.csv", index=False)
