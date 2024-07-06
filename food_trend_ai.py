import pandas as pd
from random import randint
import streamlit as st
import joblib

from modules.city_restaurant import top_restaurant_on_cities, calculate_positive_score, score
from modules.search_restaurants import get_restaurant_sentiments
from modules.dataset_insights import dataset_insights
from modules.about_dataset import about_dataset
from modules.footer import footer
from modules.developer_mode_banner import developer_mood_banner

DATASET = "Food Review Dataset of Bangladesh.xlsx"
developer_mode = True

# Streamlit app
st.set_page_config(page_title="Food Trend.AI",page_icon= "🍔")

developer_mood_banner(developer_mode)

    
st.title("🌭 Restaurant Sentiment Analysis in Bangladesh 🍔")
st.write("This app shows the sentiment analysis of restaurant reviews in Bangladesh. 🌭")


def load_dataset(path):
    return pd.read_excel(path, usecols=["ratings_int", "restaurant", "city", "preprocessed_text"])

df = joblib.load("Food Review Dataset of Bangladesh.joblib")
print(df.head())






# Sidebar menu with radio buttons
st.sidebar.title("Menu")
menu_options = [
    "Top Restaurant Based on City",
    "Search Restaurants",
    "Dataset Overview",
    "About Dataset",
    ]
selection = st.sidebar.radio("Choose a functionality", menu_options)





# Display content based on sidebar selection
if selection == "Top Restaurant Based on City":
  top_restaurant_on_cities(module_name=menu_options[0], df=df)

elif selection == "Search Restaurants":
  get_restaurant_sentiments(menu_options[1], df)
    
elif selection == "Dataset Overview":
  dataset_insights(menu_options[2], df)

elif selection == "About Dataset":
  about_dataset(menu_options[3], df)






footer()







