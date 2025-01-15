import pandas as pd
import json

file_path = "../data/cve.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Inspect the dataset structure
print("Dataset Columns:", df.columns)  # Verify column names
print(df.head())  # Preview the first few rows

# Clean and rename relevant columns
df_cleaned = df[['cwe_name', 'summary', 'cvss', 'cwe_code', 'pub_date']].copy()
df_cleaned.rename(
    columns={
        'cwe_name': 'CVE Name',
        'summary': 'Description',
        'cvss': 'Severity',
        'cwe_code': 'Weakness',
        'pub_date': 'Published Date',
    },
    inplace=True,
)

# Verify the renamed columns
print("Renamed Columns:", df_cleaned.columns)

# Normalize severity scores into levels/labels
def categorize_severity(score):
    if score < 4:
        return "Low"
    elif score < 7:
        return "Medium"
    elif score < 9:
        return "High"
    else:
        return "Critical"

df_cleaned['Severity Level'] = df_cleaned['Severity'].apply(categorize_severity)

# Convert the DataFrame to a knowledge base dictionary
knowledge_base = {}
for _, row in df_cleaned.iterrows():
    knowledge_base[row['CVE Name']] = {
        "description": row['Description'],
        "severity_score": row['Severity'],
        "severity_level": row['Severity Level'],
        "weakness": f"CWE-{row['Weakness']}" if not pd.isna(row['Weakness']) else "N/A",
        "published_date": row['Published Date'],
    }

# Save the processed data to JSON
output_path = "../data/cve_knowledge_base.json"
with open(output_path, "w") as file:
    json.dump(knowledge_base, file, indent=4)

print(f"Knowledge base saved to {output_path}")
