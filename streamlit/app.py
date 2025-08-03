import streamlit as st
import pandas as pd
import numpy as np

# Title of application
st.title("hello world")

st.write(pd.DataFrame({
    "name":["ishank","python"],
    "age":[21,56]
}))

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=("col %d" % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))