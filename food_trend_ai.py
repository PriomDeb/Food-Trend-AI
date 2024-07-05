import pandas as pd
import ast
from random import randint
import re
import string
import streamlit as st
import joblib

DATASET = "Food Review Dataset of Bangladesh.xlsx"

# Streamlit app
st.title("🌭 Restaurant Sentiment Analysis in Bangladesh 🍔")
st.write("This app shows the sentiment analysis of restaurant reviews in Bangladesh. 🌭")



def load_dataset(path):
    return pd.read_excel(path, usecols=["ratings_int", "restaurant", "city", "preprocessed_text"])

df = joblib.load("Food Review Dataset of Bangladesh.joblib")

# print(df.head())


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
    st.subheader(menu_options[0])
    unique_cities = df['city'].unique()
    selected_city = st.selectbox("Select City", sorted(unique_cities))
    
    st.subheader(f"Selected City: {selected_city}")
    
    n_top_restaurants = st.selectbox("Top Restaurants by Rating", range(1, 11))
    
    filtered_df = df[df['city'] == selected_city].nlargest(n_top_restaurants, 'ratings_int')
    
    
    st.subheader(f"Top {n_top_restaurants} Restaurants in {selected_city} by Ratings")
    if len(filtered_df) == 0:
        st.write("No restaurants found for selected city and rating range.")
    else:
        st.write(filtered_df[['restaurant', 'ratings_int']])
    
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
