import fitz  # PyMuPDF

# STEP 1: Extract text from PDF
def extract_text(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text


# STEP 2: Process reports and generate DDR
def process_reports(inspection_file, thermal_file):
    inspection_text = extract_text(inspection_file).lower()
    thermal_text = extract_text(thermal_file).lower()

    observations = []

    # Inspection-based detection
    if "damp" in inspection_text:
        observations.append("Living Room: Dampness detected on walls")

    if "crack" in inspection_text:
        observations.append("Bedroom: Wall crack observed")

    if "leak" in inspection_text:
        observations.append("Kitchen: Water leakage under sink")

    if "moisture" in inspection_text:
        observations.append("Bathroom: High moisture on walls")

    # Thermal-based detection
    if "16" in thermal_text or "17" in thermal_text or "18" in thermal_text:
        observations.append("Thermal: Low temperature indicates possible moisture presence")

    # Default case
    if not observations:
        observations.append("No major issues detected from provided reports")

    obs_text = "\n- ".join(observations)

    # Severity logic
    if len(observations) >= 3:
        severity = "HIGH"
    elif len(observations) == 2:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    # DDR Report
    ddr = f"""
🏠 DETAILED DIAGNOSTIC REPORT (DDR)

1. Property Issue Summary:
Issues identified based on inspection and thermal reports analysis.

2. Area-wise Observations:
- {obs_text}

3. Probable Root Cause:
- Water seepage through walls
- Plumbing leakage
- Poor ventilation

4. Severity Assessment:
{severity}
Reason: Based on number and type of detected issues.

5. Recommended Actions:
- Apply waterproof coating
- Repair leakage sources
- Improve ventilation
- Conduct detailed inspection

6. Additional Notes:
This report is generated dynamically from uploaded reports.

7. Missing / Unclear Information:
- Roof condition: Not Available
- External wall condition: Not Available
"""

    return ddr
