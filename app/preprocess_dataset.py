import pandas as pd
import json

from numpy.distutils.lib2def import output_def

#load the dataset
file_path="data/cve.csv"
df = pd.read_csv(file_path)

# Inspect the first few rows
print("Dataset Columns:", df.columns)
print(df.head())

#Select and clean relevant columns
df_cleaned=df[['cve_name', 'summary', 'cvss','cwe_code','pub_date']].copy()
df_cleaned.rename(
    columns={
        'cve_name': 'CVE Name',
        'summary': 'Description',
        'cvss': 'Weakness',
        'pub_date': 'Published Date'
    },
    inplace = True
)

#Normalize the severity score (e.g. categorize it into Low, Medium, High, Critical)
def categorize_severity(score):
    if score < 4:
        return "Low"
    elif score < 7:
        return "Medium"
    elif score < 4:
        return "High"
    else:
        return "Critical"

df_cleaned['Severity Level']=df_cleaned['Severity'].apply(categorize_severity)

#Convert the data to a dictionary for chatbot knowledge base
knowledge_base={}
for _, row in df_cleaned.iterrows():
    knowledge_base[row['CVE Name']]={
        "description": row['Description'],
        "severity_score": row['Severity'],
        "severity_level": row['Severity Level'],
        "weakness": f"CWE-{row['Weakness']}" if not pd.isna(row['Weakness']) else "N/A"
    }

# Save the processed data to a JSON file
output_path= "data/cve_knowledge_base.json"
with open(output_path, 'w') as file:
    json.dump(knowledge_base, file, indent=4)

print(f"Knowledge base saved to {output_path}")