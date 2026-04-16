from pypdf import PdfReader
from openai import OpenAI

client = OpenAI(api_key="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")


# Extract text
def extract_text(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


# AI processing
def generate_ddr(inspection_text, thermal_text):

    prompt = f"""
You are an expert building inspection analyst.

Using the following two reports:

INSPECTION REPORT:
{inspection_text}

THERMAL REPORT:
{thermal_text}

Generate a structured DDR report with:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

Rules:
- Do NOT invent data
- If missing → "Not Available"
- If conflict → mention clearly
- Avoid duplicate points
- Use simple language
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# MAIN
inspection_text = extract_text("inspection.pdf")
thermal_text = extract_text("thermal.pdf")

ddr = generate_ddr(inspection_text, thermal_text)

# Save output
with open("output/DDR_Report.txt", "w") as f:
    f.write(ddr)

print("✅ DDR Generated Successfully!")
