import pandas as pd
import ast
from random import randint
import re
import string
import streamlit as st
import joblib

DATASET = "Food Review Dataset of Bangladesh.xlsx"
developer_mode = True

# Streamlit app
st.set_page_config(page_title="Food Trend.AI",page_icon= "🍔")
html_code = """
<style>
@keyframes typing {
  0% { width: 0; }
  50% { width: 26ch; }
  100% { width: 0; }
}

@keyframes blink-caret {
  from, to { border-color: transparent; }
  50% { border-color: orange; }
}

.typewriter {
  text-align: center;
  overflow: hidden;
  border-right: .15em solid orange;
  white-space: nowrap;
  margin: 0 auto;
  animation: typing 6s steps(19, end) infinite, blink-caret .75s step-end infinite;
  width: 19ch; /* Set width to match character count */
  display: inline-block;
}

.development{
    text-align: center;
    color: white;
    background-color: red;
    border-radius: 10px;
    height: 26px;
}
</style>

<div class="development">
<div class="typewriter">
  🚀 Development View
</div>
</div>
"""
if developer_mode:
    
    st.markdown(html_code, unsafe_allow_html=True)
    
st.title("🌭 Restaurant Sentiment Analysis in Bangladesh 🍔")
st.write("This app shows the sentiment analysis of restaurant reviews in Bangladesh. 🌭")


def load_dataset(path):
    return pd.read_excel(path, usecols=["ratings_int", "restaurant", "city", "preprocessed_text"])

df = joblib.load("Food Review Dataset of Bangladesh.joblib")


def calculate_positive_score(ratings):
    positive_ratings = ratings[ratings >= 3]
    score = (len(positive_ratings) / len(ratings)) * 100 if len(ratings) > 0 else 0
    return score

def calculate_negative_percentage(ratings):
    positive_ratings = ratings[ratings < 3]
    score = (len(positive_ratings) / len(ratings)) * 100 if len(ratings) > 0 else 0
    return score

def calculate_neutral_percentage(ratings):
    positive_ratings = ratings[ratings == 3]
    score = (len(positive_ratings) / len(ratings)) * 100 if len(ratings) > 0 else 0
    return score

def calculate_positive_percentage(ratings):
    positive_ratings = ratings[ratings >= 4]
    score = (len(positive_ratings) / len(ratings)) * 100 if len(ratings) > 0 else 0
    return score


# Sidebar menu with radio buttons
st.sidebar.title("Menu")
menu_options = [
    "Top Restaurant Based on City",
    "Search Restaurants",
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
        
        def score(score):
            return f"{score:.2f}%"
        
        try:
            st.dataframe(filtered_df.style.background_gradient(cmap='Greens', subset=['Positive Score']).\
                set_properties(**{'text-align': 'center'}).format({'Positive Score': '{:.2f}%'}), width=600)
        except:
            filtered_df["Positive Score"] = filtered_df["Positive Score"].apply(score)
            st.dataframe(filtered_df, width=600)

elif selection == "Search Restaurants":
  st.subheader("Search Restaurants")
  
  unique_restaurants = df['restaurant'].unique()
  selected_restaurant = st.selectbox("Select Restaurant", sorted(unique_restaurants))
  
  filtered_df = df[df['restaurant'] == selected_restaurant].groupby('restaurant')['ratings_int'].apply(calculate_positive_percentage).reset_index()
  filtered_df.columns = ['Restaurant', 'Positive Sentiment']
  
  negative_scores = df[df['restaurant'] == selected_restaurant].groupby('restaurant')['ratings_int'].apply(calculate_negative_percentage).reset_index()
  negative_scores.columns = ['Restaurant', 'Negative Sentiment']
  filtered_df = filtered_df.merge(negative_scores, on='Restaurant', how='left')
  
  neutral_scores = df[df['restaurant'] == selected_restaurant].groupby('restaurant')['ratings_int'].apply(calculate_neutral_percentage).reset_index()
  neutral_scores.columns = ['Restaurant', 'Neutral Sentiment']
  filtered_df = filtered_df.merge(neutral_scores, on='Restaurant', how='left')
  
  if len(filtered_df) == 0:
    st.write("No restaurants found for selected city.")
    
  else:
    filtered_df = filtered_df.reset_index(drop=True)
    filtered_df.index += 1
    
    st.dataframe(filtered_df, width=600)
    
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

developer = """

---
# 

## Contact 🌱

[![Website](https://img.shields.io/badge/priomdeb.com-teal)](https://priomdeb.com)
[![GitHub](https://img.shields.io/badge/GitHub-black)](https://github.com/PriomDeb)
[![Mail](https://img.shields.io/badge/priom@priomdeb.com-yellow)](mailto:priom@priomdeb.com)
[![GitHub](https://img.shields.io/badge/GitHub-black)](https://github.com/PriomDeb)

"""

st.caption(developer)

footer = """
<style>
@keyframes typing {
  0% { width: 0; }
  50% { width: 26ch; }
  100% { width: 0; }
}

@keyframes blink-caret {
  from, to { border-color: transparent; }
  50% { border-color: orange; }
}

.typewriter {
  text-align: center;
  overflow: hidden;
  border-right: .15em solid orange;
  white-space: nowrap;
  margin: 0 auto;
  animation: typing 4s steps(19, end) infinite, blink-caret .75s step-end infinite;
  width: 19ch; /* Set width to match character count */
  display: inline-block;
}

.copyright{
    text-align: center;
}
</style>

<div class="copyright">
<div class="">
  Made with ❤️ by Priom Deb
</div>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)



