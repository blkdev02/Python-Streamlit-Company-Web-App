import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.title("The Best Company")
content = "The Best Company was created in 1787. \
The main purpose of the company is to create the best products"
st.write(content)
st.subheader("Our Team")


col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")




with col1:

    for index, row in df[:4].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])


with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])


with col3:
    for index,row in df[8:].iterrows():
        st.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
