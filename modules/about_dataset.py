import pandas as pd
import streamlit as st


def about_dataset(module_name, df):
    st.subheader(module_name)
    st.write("Total number of reviews:", df.shape[0])
    st.write("Number of unique restaurants:", df["restaurant"].nunique())
    st.write("Number of unique cities:", df["city"].nunique())
    
    st.subheader("Sample Reviews")
    st.write(df.sample(5))

