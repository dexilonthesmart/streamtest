import streamlit as st
import pandas as pd

st.title("# Team it works")

st.write("# Surprise 👋")

st.write("Talking to the dataset")


df = pd.read_csv("mini model dataset.csv")

head = df.head()

st.text(head)
