import pandas as pd
from random import randint
import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from wordcloud import WordCloud
import seaborn as sns

from tools.load_dataset import load_from_serialized



DATASET_JOBLIB = "Food Review Dataset of Bangladesh.joblib"
df = load_from_serialized(DATASET_JOBLIB)




def white_spaces():
    st.write("\n # ")




def number_of_reviews_per_city():
    st.write("## Number of Reviews per City")
    st.text("This bar chart shows the total number of reviews for each city.")
    reviews_per_city = df['city'].value_counts()
    st.bar_chart(reviews_per_city)




def number_of_reviews_per_restaurant():
    st.write("## Number of Reviews per Restaurant")
    st.text("This bar chart shows the total number of reviews for the top 10 restaurants.")
    reviews_per_restaurant = df['restaurant'].value_counts().head(10)
    st.bar_chart(reviews_per_restaurant)




def distribution_of_ratings():
    st.write("## Distribution of Ratings")
    st.text("This bar chart shows the distribution of ratings across all reviews.")
    ratings_distribution = df['ratings_int'].value_counts().sort_index()
    st.bar_chart(ratings_distribution)




def bar_chart_of_average_ratings_per_city():
    st.write("## Average Ratings per City")
    st.text("This bar chart shows the average ratings for each city.")
    avg_ratings_per_city = df.groupby('city')['ratings_int'].mean().sort_values(ascending=False)
    st.bar_chart(avg_ratings_per_city)




def bar_chart_of_top_restaurants_by_number_of_reviews():
    st.write("## Top Restaurants by Number of Reviews")
    st.text("This bar chart shows the top 10 restaurants based on the number of reviews.")
    top_restaurants_by_reviews = df['restaurant'].value_counts().head(10)
    st.bar_chart(top_restaurants_by_reviews)




def histogram_of_ratings_distribution():
    st.write("## Histogram of Ratings Distribution")
    st.text("This histogram shows the distribution of ratings across all reviews.")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df['ratings_int'], bins=5, kde=True, ax=ax)
    st.pyplot(fig)




def pairplot_of_restaurants():
    st.write("## Pairplot of Restaurants")
    st.text("This plot shows the distribution of ratings across different restaurants.")
    plot = sns.pairplot(df, hue ='restaurant')
    st.pyplot(plot)




def pairplot_of_cities():
    st.write("## Pairplot of Cities")
    st.text("This plot shows the distribution of ratings across different cities.")
    plot = sns.pairplot(df, hue ='city')
    st.pyplot(plot)


def wordcloud():
    st.write("## Word Cloud of Review Text")
    st.text("This word cloud visualizes the most frequent words in the review texts.")
    all_text = " ".join(df['preprocessed_text'].astype(str))
    word_cloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

def dataset_insights(module_name, df):
    st.subheader(module_name)
    
    number_of_reviews_per_city()
    white_spaces()
    
    number_of_reviews_per_restaurant()
    white_spaces()
    
    distribution_of_ratings()
    white_spaces()
    
    bar_chart_of_average_ratings_per_city()
    white_spaces()
    
    bar_chart_of_top_restaurants_by_number_of_reviews()
    white_spaces()
    
    histogram_of_ratings_distribution()
    white_spaces()
    
    pairplot_of_restaurants()
    white_spaces()
    
    pairplot_of_cities()
    white_spaces()
    
    wordcloud()
    

