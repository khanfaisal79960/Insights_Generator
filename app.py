# app.py
import streamlit as st
import pandas as pd
from utils.ranker import analyze_raw_data
from utils.report_generator import generate_html_report

st.set_page_config(page_title="📊 AI-Driven Influencer Insights", layout="centered")
st.title("🤖 Upload File & Let AI Do the Rest")

uploaded_file = st.file_uploader("\U0001F4C2 Upload your Excel file", type=["xlsx"])

if uploaded_file:
    try:
        # Step 1: Load file
        xls = pd.ExcelFile(uploaded_file)
        sheet = st.selectbox("\U0001F4C4 Select a Sheet", xls.sheet_names)
        df = pd.read_excel(xls, sheet_name=sheet)

        st.success("✅ File loaded successfully. AI is now analyzing your data...")

        if st.button("\U0001F680 Generate AI Report"):
            with st.spinner("Analyzing with LLaMA 3 via OpenRouter..."):
                summary = analyze_raw_data(df)
                st.subheader("📋 AI-Powered Summary")

                # Frontend Clean Format
                for section in summary.strip().split("\n\n"):
                    if section.lower().startswith(("top influencers", "influencers to pause", "optimization suggestions")):
                        st.markdown(f"### {section.split(':')[0]}")
                        items = section.split(':')[1].strip().split("\n")
                        st.markdown("\n".join([f"- {i.strip('- ')}" for i in items if i.strip()]))
                    else:
                        st.markdown(section)

                st.markdown("---")
                st.markdown("✅ **Made by [Khan Faisal](https://khanfaisal.netlify.app)**")

                generate_html_report(summary)
                with open("influencer_report.pdf", "rb") as f:
                    st.download_button("\U0001F4E5 Download PDF Report", f, file_name="influencer_report.pdf")

    except Exception as e:
        st.error(f"❌ Error: {e}")
else:
    st.info("\U0001F4C1 Upload an Excel file to begin.")