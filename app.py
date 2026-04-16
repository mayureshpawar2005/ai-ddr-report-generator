import streamlit as st
from main import process_reports

st.set_page_config(page_title="DDR Generator", layout="centered")

st.title("🧠 AI DDR Report Generator")

st.write("Upload Inspection and Thermal Reports to generate a structured DDR report.")

inspection_file = st.file_uploader("📄 Upload Inspection Report", type="pdf")
thermal_file = st.file_uploader("🌡️ Upload Thermal Report", type="pdf")

if st.button("Generate DDR"):
    if inspection_file and thermal_file:
        result = process_reports(inspection_file, thermal_file)

        st.subheader("📋 Generated DDR Report")
        st.markdown(result)

    else:
        st.error("⚠️ Please upload both files")
