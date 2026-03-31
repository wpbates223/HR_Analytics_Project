import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "clean_hr_data.csv")

df = pd.read_csv(file_path)

features = [
    "monthlyincome",
    "yearsatcompany",
    "worklifebalance",
    "performancerating"
]

X = df[features]
y = df["attrition_flag"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

df["attrition_risk_score"] = model.predict_proba(X)[:, 1]

def categorize_risk(score):
    if score > 0.7:
        return "High Risk"
    elif score > 0.4:
        return "Medium Risk"
    else:
        return "Low Risk"
    
df["risk_category"] = df["attrition_risk_score"].apply(categorize_risk)

output_path = os.path.join(BASE_DIR, "data", "hr_with_risk_scores.csv")
df.to_csv(output_path, index=False)

print("Model complete - risk scores generated")


