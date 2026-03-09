import requests
import time
def cve_search(cve_id):
  response=requests.get(f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}")

  if response.status_code == 200:
    data=response.json()
    # Check if 'vulnerabilities' key exists and is not empty
    if not data.get("vulnerabilities"):
        return None, None, None # No vulnerabilities found for this CVE ID

    cve_data = data["vulnerabilities"][0]["cve"]
    description = cve_data["descriptions"][0]["value"]
    references = cve_data["references"]

    cvss_score = None # Initialize cvss_score

    metrics = cve_data.get("metrics")
    if metrics:
        if "cvssMetricV31" in metrics and metrics["cvssMetricV31"]:
            cvss_score = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]
        elif "cvssMetricV2" in metrics and metrics["cvssMetricV2"]:
            # Fallback to CVSS v2 if V3.1 is not available
            cvss_score = metrics["cvssMetricV2"][0]["cvssData"]["baseScore"]

    return description,references,cvss_score
  else:
    return None,None,None

cve_id=input("Provide a CVE-ID:").strip()
description,references,cvss_score=cve_search(cve_id)
result=""

if cvss_score is None:
  result = "Unknown"
elif cvss_score < 4.0: # CVSS v3.1: 0.1-3.9 Low
  result = "Low"
elif cvss_score < 7.0: # CVSS v3.1: 4.0-6.9 Medium
  result = "Medium"
elif cvss_score < 9.0: # CVSS v3.1: 7.0-8.9 High
  result = "High"
else: # CVSS v3.1: 9.0-10.0 Critical
  result = "Critical"

dic={"Description":description,
     "References":references,
     "Metric":[cvss_score,result]}

print(dic)
