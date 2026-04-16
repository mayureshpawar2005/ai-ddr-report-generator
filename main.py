import pdfplumber
import json

# Extract text
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


# Dummy processing (you can keep your AI logic here)
def process_reports(inspection_file, thermal_file):
    inspection_text = extract_text(inspection_file)
    thermal_text = extract_text(thermal_file)

    # Simple demo DDR (replace with your AI logic if working)
    ddr = f"""
    PROPERTY ISSUE SUMMARY:
    Moisture-related issues detected.

    AREA OBSERVATIONS:
    Living Room: Dampness observed
    Kitchen: Leakage detected

    ROOT CAUSE:
    Possible water seepage

    SEVERITY:
    High

    RECOMMENDED ACTION:
    Waterproofing required

    MISSING INFO:
    Not Available
    """

    return ddr