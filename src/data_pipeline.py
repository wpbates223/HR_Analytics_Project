import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw_hr_data.csv")

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Create attrition flag
df["attrition_flag"] = df["attrition"].map({"Yes": 1, "No": 0})

# Create tenure groups
df["tenure_group"] = pd.cut(
    df["yearsatcompany"],
    bins=[0,2,5,10,20],
    labels=["0-2","3-5","6-10","10+"]
)

# Save the cleaned dataset
df.to_csv("data/clean_hr_data.csv", index=False)

print("Data pipeline completed successfully. Cleaned data saved to 'data/clean_hr_data.csv'.")