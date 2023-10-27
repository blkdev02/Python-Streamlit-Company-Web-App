import streamlit as st
from send_email import send_email

st.header("Contact Us")


with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    option = st.selectbox("What topic do you want to discuss?", ("Job Inquiries", "Project Proposals", "Other"), key="options")
    message = st.text_area("Your message")
    raw_message = f"""\
Subject: New Email from {user_email} Topic - {option}

From: {user_email}
Topic: {option}
{message}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(raw_message)
        st.info("Your message was send. Thank you.")
