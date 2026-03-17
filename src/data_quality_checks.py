import pandas as pd

df = pd.read_csv("data/clean_hr_data.csv")

# Check for missing IDs
assert df["employeenumber"].isnull().sum() == 0

# Check for salary values
assert df["monthlyincome"].min() > 0

# Check attrition flag values
assert df["attrition_flag"].isin([0,1]).all()

print("All data quality checks passed successfully.")