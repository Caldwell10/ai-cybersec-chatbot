import os
import json

#Dynamically resolve the path to the JSON file based on the script's location
base_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(base_dir, "../data/cve_knowledge_base.json")

# Load the knowledge base
with open(json_file_path ,"r") as file:
    knowledge_base =json.load(file)

#Function that takes a CVE name or keyword and retrieves the relevant data
def get_cve_info(cve_name):
    cve_name = cve_name.strip()  # Remove leading/trailing spaces
    for key in knowledge_base.keys():
        if cve_name.lower() == key.strip().lower():  # Case-insensitive match, strip spaces
            cve_data = knowledge_base[key]
            return (
                f"**CVE Name:** {key.strip()}\n"
                f"**Description:** {cve_data['description']}\n"
                f"**Severity:** {cve_data['severity_level']} "
                f"({cve_data['severity_score']})\n"
                f"**Weakness:** {cve_data['weakness']}\n"
                f"**Published Date:** {cve_data['published_date']}"
            )
    return "Sorry, I couldn't find any information on that CVE."

#search for CVEs by keywords within the description,
def search_cve_by_keyword(keyword):
    results = []
    for key, cve_data in knowledge_base.items():
        if keyword.lower() in cve_data['description'].lower():
            results.append(f"**CVE Name:** {key.strip()}\n"
                           f"**Description:** {cve_data['description']}\n"
                           f"**Severity:** {cve_data['severity_level']} "
                           f"({cve_data['severity_score']})\n"
                           f"**Weakness:** {cve_data['weakness']}\n"
                           f"**Published Date:** {cve_data['published_date']}\n")
            return "\n\n".join(results) if results else "No CVEs found matching that keyword."

# Function that enables filtering by severity levels(Low, Medium, High etc)
def filter_cve_by_severity(severity):
    severity = severity.capitalize()
    results = [f"**CVE Name:** {key.strip()}\n**Severity:** {data['severity_level']} ({data['severity_score']})"
               for key, data in knowledge_base.items() if data['severity_level'] == severity]
    return "\n\n".join(results) if results else f"No CVEs found with severity '{severity}'."

