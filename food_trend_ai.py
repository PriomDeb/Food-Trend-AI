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

from tools.load_dataset import load_from_serialized

DATASET = "Food Review Dataset of Bangladesh.xlsx"
DATASET_JOBLIB = "./Food Review Dataset of Bangladesh.joblib"
developer_mode = True

# Streamlit app
st.set_page_config(page_title="Food Trend.AI",page_icon= "🍔")

developer_mood_banner(developer_mode)


st.title("🍔 Food Trend.AI")
st.text("This app shows the sentiment analysis of restaurant reviews in Bangladesh. 🌭")


df = load_from_serialized(DATASET_JOBLIB)
print(df.head())






# Sidebar menu with radio buttons
st.sidebar.title("Menu")
menu_options = [
    "Top Restaurant Based on City",
    "Search Restaurants",
    "Dataset Insights",
    "About Dataset",
    ]
selection = st.sidebar.radio("Choose a functionality", menu_options)





# Display content based on sidebar selection
if selection == "Top Restaurant Based on City":
  top_restaurant_on_cities(module_name=menu_options[0], df=df)

elif selection == "Search Restaurants":
  get_restaurant_sentiments(menu_options[1], df)
    
elif selection == "Dataset Insights":
  dataset_insights(menu_options[2], df)

elif selection == "About Dataset":
  about_dataset(menu_options[3], df)






footer()







