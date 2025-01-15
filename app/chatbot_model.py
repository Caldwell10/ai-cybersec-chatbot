import json

# Load the knowledge base
with open("../data/cve_knowledge_base.json","r") as file:
    knowledge_base =json.load(file)

#Function that takes a CVE name or keyword and retrieves the relevant data
def get_cve_info(cve_name):
    cve_name = cve_name.upper() # Ensure case-insensitivity
    if cve_name in knowledge_base:
        cve_data = knowledge_base[cve_name]
        return(
            f"**CVE Name:** {cve_name}\n"
            f"**Description:** {cve_data['description']}\n"
            f"**Severity:** {cve_data['severity_level']} "
            f"({cve_data['severity_score']})\n"
            f"**Weakness:** {cve_data['weakness']}\n"
            f"**Published Date:** {cve_data['published_date']}"
        )
    else:
        return "Sorry, I couldnt find any information on that CVE."




