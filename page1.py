import streamlit as st

st.title("# Team it works")

st.write("# Surprise 👋")

# Group by input anger level and calculate the mean fear for each level
grouped_df = df.groupby('input_fear_ordinal')['output_anger_ordinal'].mean().reset_index()

