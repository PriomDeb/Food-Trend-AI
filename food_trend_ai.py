import pandas as pd
import ast
from random import randint
import re
import string
import streamlit as st

DATASET = "Food Review Dataset of Bangladesh.xlsx"

# Streamlit app
st.title("🌭 Restaurant Sentiment Analysis in Bangladesh 🍔")
st.write("This app shows the sentiment analysis of restaurant reviews in Bangladesh. 🌭")



def load_dataset(path):
    return pd.read_excel(path, usecols=["ratings_int", "restaurant", "city", "preprocessed_text"])

df = load_dataset(DATASET)

print(df.head())


# Sidebar menu with radio buttons
st.sidebar.title("Menu")
menu_options = [
    "Top Restaurant Based on City",
    "Dataset Overview", 
    "Statistics", 
    "Ratings Distribution", 
    "Sample Reviews"
    ]
selection = st.sidebar.radio("Choose a functionality", menu_options)

# Display content based on sidebar selection
if selection == "Top Restaurant Based on City":
    unique_cities = df['city'].unique()
    selected_city = st.selectbox("Select City", sorted(unique_cities))
    
    st.subheader(menu_options[0])
    st.write(unique_cities)
    
elif selection == "Dataset Overview":
    st.subheader("Dataset Overview")
    st.write(df.head())

elif selection == "Statistics":
    st.subheader("Statistics")
    st.write("Total number of reviews:", df.shape[0])
    st.write("Number of unique restaurants:", df["restaurant"].nunique())
    st.write("Number of unique cities:", df["city"].nunique())

elif selection == "Ratings Distribution":
    st.subheader("Ratings Distribution")
    st.bar_chart(df["ratings_int"].value_counts())

elif selection == "Sample Reviews":
    st.subheader("Sample Reviews")
    st.write(df["preprocessed_text"].sample(5))
