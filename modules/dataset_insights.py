import pandas as pd
from random import randint
import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from wordcloud import WordCloud
import seaborn as sns

def dataset_insights(module_name, df):
    st.subheader(module_name)
    
    # Number of reviews per city
    st.write("## Number of Reviews per City")
    reviews_per_city = df['city'].value_counts()
    st.bar_chart(reviews_per_city)
    
    # Number of reviews per restaurant
    st.write("## Number of Reviews per Restaurant")
    reviews_per_restaurant = df['restaurant'].value_counts().head(10)
    st.bar_chart(reviews_per_restaurant)
    
    # Distribution of ratings
    st.write("## Distribution of Ratings")
    ratings_distribution = df['ratings_int'].value_counts().sort_index()
    st.bar_chart(ratings_distribution)
    
    
    # Word cloud of preprocessed text
    st.write("## Word Cloud of Review Text")
    all_text = " ".join(df['preprocessed_text'].astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
    
    
    
    st.write("## Pairplot of Restaurants")
    st.text("This plot shows the distribution of ratings across different restaurants.")
    # sns.set_style('darkgrid')
    plot = sns.pairplot(df, hue ='restaurant')
    st.pyplot(plot)
    
    st.write("## Pairplot of Cities")
    st.text("This plot shows the distribution of ratings across different cities.")
    plot = sns.pairplot(df, hue ='city')
    st.pyplot(plot)
    
    # Bar chart of average ratings per city
    st.write("## Average Ratings per City")
    avg_ratings_per_city = df.groupby('city')['ratings_int'].mean().sort_values(ascending=False)
    st.bar_chart(avg_ratings_per_city)
    
    # Bar chart of top restaurants by number of reviews
    st.write("## Top Restaurants by Number of Reviews")
    top_restaurants_by_reviews = df['restaurant'].value_counts().head(10)
    st.bar_chart(top_restaurants_by_reviews)
    
    # Histogram of ratings distribution
    st.write("## Histogram of Ratings Distribution")
    # st.text("This histogram shows the distribution of ratings across all reviews.")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df['ratings_int'], bins=5, kde=True, ax=ax)
    st.pyplot(fig)
    
    
    # Word cloud of most frequent words in review text
    st.write("## Word Cloud of Most Frequent Words in Review Text")
    all_text = " ".join(df['preprocessed_text'].astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

