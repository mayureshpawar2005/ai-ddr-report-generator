import streamlit as st
from main import process_reports

st.title("AI DDR Report Generator")

inspection_file = st.file_uploader("Upload Inspection Report", type="pdf")
thermal_file = st.file_uploader("Upload Thermal Report", type="pdf")

if st.button("Generate DDR"):
    if inspection_file and thermal_file:
        result = process_reports(inspection_file, thermal_file)

        st.subheader("Generated DDR Report")
        st.text(result)

    else:
        st.error("Please upload both files")