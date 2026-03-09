# 🛡️ CVE Bilingual Reporter

A Python-based security tool that fetches vulnerability data from the **National Vulnerability Database (NVD)** and generates a professional, bilingual (English & Spanish) assessment in Microsoft Word format.



## 🌟 Overview

This script automates the manual task of looking up CVE details and formatting them for stakeholders. It queries the NIST API, parses the JSON response, determines the CVSS severity, translates the technical description into Spanish, and exports everything into a structured `.docx` file.

## 🚀 Features

- **NVD API v2.0 Integration:** Fetches real-time data using the latest NIST standards.
- **Smart CVSS Scoring:** Prioritizes CVSS v3.1 metrics with a fallback to v2.0.
- **Automated Translation:** Uses `deep-translator` to provide an English-to-Spanish technical summary.
- **Professional Formatting:** Utilizes `python-docx` for headers, bulleted lists, and page breaks.
- **Cross-Platform Auto-Open:** Automatically opens the report in your default Word processor (Windows, Mac, or Linux).



## 🛠️ Installation

Ensure you have Python 3.9+ installed. You will need to install the following dependencies:

```bash
pip install python-docx requests deep_translator


