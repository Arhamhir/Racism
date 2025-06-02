import streamlit as st
import re
import requests
from datetime import datetime

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("<h1 style='text-align: center;'>Contact & Feedback</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Have suggestions, found a bug, or just want to say hi? We'd love to hear from you!</p>", unsafe_allow_html=True)
st.markdown("---")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Gmail (required)")
    message = st.text_area("Share your thoughts, feedback, or questions", height=150)
    submitted = st.form_submit_button("Send")

    if submitted:
        if not re.match(r"^[\w\.-]+@gmail\.com$", email):
            st.error("Please enter a valid Gmail address.")
        elif name.strip() == "" or message.strip() == "":
            st.error("Name and message cannot be empty.")
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            payload = {
                "name": name,
                "email": email,
                "message": message,
                "timestamp": timestamp
            }

            url = "https://script.google.com/macros/s/AKfycby79ybNYK4LewGTRsVpBSGSh2XY2hYdmBkbOHADk-31TmmrsMmWvm08Dt5GC6nCnbRj/exec"

            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    st.success("✅ Feedback submitted successfully! Thank you for your time.")
                else:
                    st.warning("❌ Failed to submit feedback. Please try again later.")
            except Exception as e:
                st.error(f"⚠️ An error occurred: {e}")


st.markdown("""
<div style='text-align: center;'>
    <a style='color: #FFD700; padding:0px 10px;' href="https://github.com/Arhamhir" target="_blank">GitHub</a> |
    <a style='color: #FFD700; padding:0px 10px;' href="https://www.linkedin.com/in/arham-tahir-95626a28a/" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)


st.markdown("---")
st.markdown("""
    <h5 style='text-align: center;'>Created by <code>Syed Ashtar Ali Zaidi</code> & <code>Muhammad Arham Tahir</code></h5>
""", unsafe_allow_html=True)
