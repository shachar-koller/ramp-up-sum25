import streamlit as st
import pandas as pd
import numpy as np

st.write("## hello streamlit")

char_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["a", "b", "c"]
)

st.write("#### Here's a dataframe chart")
st.bar_chart(char_data)
st.write("#### Here's another dataframe chart")
st.line_chart(char_data)

st.divider()
input = st.text_input("What's your favorite programmign language?")
st.divider()
st.write(f"your favorite language is {input}")
st.divider()
is_clicked = st.button('click here')
st.divider()

data = pd.read_csv("data.csv")
st.write(data)