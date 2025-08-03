import streamlit as st 
import pandas as pd

st.title("Streamlit Text input")

name = st.text_input("enter your name")
age = st.slider("Select your age", min_value=10, max_value=50, step=1)
options = ["-- Select --", "Java", "Python", "JavaScript"]
lang = st.selectbox("Select the programming language", options)

if lang != "-- Select --":
    st.write(f"You selected: {lang}")
else:
    st.warning("Please select a programming language.")

if name:
    st.write("Hello , %s" % name)
    st.write(f"your age is {age}")

upload_file = st.file_uploader("chose a csv file",type=["csv"])

if upload_file!=None:
    df = pd.read_csv(upload_file)
    st.write(df)

st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

if st.button("Send balloons!"):
    st.balloons()

