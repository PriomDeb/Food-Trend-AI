import pandas as pd
import ast
from random import randint
import re
import string
import streamlit as st
import joblib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from wordcloud import WordCloud
import seaborn as sns

from tools.helper_functions import calculate_positive_score, score



def top_restaurant_on_cities(module_name, df):
    st.subheader(module_name)
    unique_cities = df['city'].unique()
    selected_city = st.selectbox("Select City", sorted(unique_cities))
    
    # Subheader of Selected City
    st.subheader(f"Selected City: {selected_city}")
    
    # Select Number of Top Restaurants to See
    n_top_restaurants = st.selectbox("Top Restaurants by Rating", range(1, 51))
    
    # Filter Top Number of Restaurants
    # Filter and sort restaurants by selected city and highest positive ratings percentage
    filtered_df = df[df['city'] == selected_city].\
                  groupby('restaurant')['ratings_int'].apply(calculate_positive_score).reset_index()
    
    
    filtered_df.columns = ['Restaurants', 'Positive Score']
    filtered_df = filtered_df.nlargest(n_top_restaurants, 'Positive Score')
    
    print(filtered_df.head())
    # filtered_df['Positive Score'] = filtered_df['Positive Score'].apply(lambda x: f"{x:.2f}%")
    

    # Display top restaurants based on highest positive ratings percentage with score
    st.subheader(f"Top {n_top_restaurants} Restaurants in {selected_city} by Positive Ratings Percentage")
    if len(filtered_df) == 0:
        st.write("No restaurants found for selected city.")
    else:
        filtered_df = filtered_df.reset_index(drop=True)
        filtered_df.index += 1
        
        # st.table(filtered_df)
        
        try:
            st.dataframe(filtered_df.style.background_gradient(cmap='Greens', subset=['Positive Score']).\
                set_properties(**{'text-align': 'center'}).format({'Positive Score': '{:.2f}%'}), width=600)
        except:
            filtered_df["Positive Score"] = filtered_df["Positive Score"].apply(score)
            st.dataframe(filtered_df, width=600)

