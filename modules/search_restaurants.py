import pandas as pd
from random import randint
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from tools.helper_functions import calculate_positive_percentage, calculate_neutral_percentage, calculate_negative_percentage, score






def get_restaurant_sentiments(module_name, df):
  st.subheader(module_name)
  
  unique_restaurants = df['restaurant'].unique()
  selected_restaurant = st.selectbox("Select Restaurant", sorted(unique_restaurants))
  
  filtered_df = df[df['restaurant'] == selected_restaurant].groupby('restaurant')['ratings_int'].apply(calculate_positive_percentage).reset_index()
  filtered_df.columns = ['Restaurant', 'Positive Sentiment']
  
  neutral_scores = df[df['restaurant'] == selected_restaurant].groupby('restaurant')['ratings_int'].apply(calculate_neutral_percentage).reset_index()
  neutral_scores.columns = ['Restaurant', 'Neutral Sentiment']
  filtered_df = filtered_df.merge(neutral_scores, on='Restaurant', how='left')
  
  negative_scores = df[df['restaurant'] == selected_restaurant].groupby('restaurant')['ratings_int'].apply(calculate_negative_percentage).reset_index()
  negative_scores.columns = ['Restaurant', 'Negative Sentiment']
  filtered_df = filtered_df.merge(negative_scores, on='Restaurant', how='left')
  
  positive = filtered_df["Positive Sentiment"].values[0]
  neutral = filtered_df["Neutral Sentiment"].values[0]
  negative = filtered_df["Negative Sentiment"].values[0]
  
  filtered_df["Positive Sentiment"] = filtered_df["Positive Sentiment"].apply(score)
  filtered_df["Neutral Sentiment"] = filtered_df["Neutral Sentiment"].apply(score)
  filtered_df["Negative Sentiment"] = filtered_df["Negative Sentiment"].apply(score)
  
  positive, neutral, negative = round(positive, 2), round(neutral, 2), round(negative, 2)
  
  print(positive, negative, neutral)
  
  
  
  
  
  
  
  if len(filtered_df) == 0:
    st.write("No restaurants found for selected city.")
    
  else:
    filtered_df = filtered_df.reset_index(drop=True)
    filtered_df.index += 1
    
    st.dataframe(filtered_df, width=600)
    
    sentiment_data = {
    'Sentiment': ['Positive', 'Negative', 'Neutral'],
    'Score': [positive, negative, neutral]
    }
  
  sentiment_df = pd.DataFrame(sentiment_data)
  
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  
  x = [0, 1, 2]
  y = [0, 0, 0]
  z = [0, 0, 0]
  dx = dy = [0.4, 0.4, 0.4]
  dz = [positive, negative, neutral]
  
  colors = ['#4CAF50', '#F44336', '#FFC107']
  
  ax.bar3d(x, y, z, dx, dy, dz, color=colors)
  
  ax.set_xticks([0.25, 1.25, 2.25])
  ax.set_xticklabels(['Positive', 'Negative', 'Neutral'])
  ax.set_ylabel('')
  ax.set_zlabel('Score')
  ax.set_yticks([])
  
  ax.set_title(f"{selected_restaurant} \nSentiment Analysis - 3D Bar Chart")
  st.pyplot(fig)
  
  st.write("\n # ")
  
  # Pie Chart
  labels = ['Positive', 'Negative', 'Neutral']
  sizes = [positive, negative, neutral]
  colors = ['#4CAF50', '#F44336', '#FFC107']
  explode = (0.1, 0, 0)  # explode the 1st slice (i.e. 'Positive')
  
  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
  
  ax1.axis('equal')
  ax1.set_title(f"{selected_restaurant} \nSentiment Analysis - Pie Chart")
  st.pyplot(fig1)
  
  st.write("\n # ")
  
  sentiment_df.set_index('Sentiment', inplace=True)
  fig2, ax2 = plt.subplots()
  sentiment_df.T.plot(kind='bar', stacked=True, color=colors, ax=ax2)
  ax2.set_title(f"{selected_restaurant} \nSentiment Analysis - Stacked Bar Chart")
  ax2.set_ylabel('Score')
  ax2.legend(title='Sentiment')
  st.pyplot(fig2)
  
  
  
  st.write("\n # ")
  
  
  selected_restaurant_df = df[df['restaurant'] == selected_restaurant]
  
  positive_threshold = 4
  negative_threshold = 2
  
  
  positive_text = ' '.join(selected_restaurant_df[selected_restaurant_df['ratings_int'] >= positive_threshold]['preprocessed_text'])
  negative_text = ' '.join(selected_restaurant_df[selected_restaurant_df['ratings_int'] <= negative_threshold]['preprocessed_text'])
  neutral_text = ' '.join(selected_restaurant_df[(selected_restaurant_df['ratings_int'] > negative_threshold) & (selected_restaurant_df['ratings_int'] < positive_threshold)]['preprocessed_text'])
  
  with st.spinner('Wait for it...'):
      positive_wc = WordCloud(width=1600, height=800, background_color='white', colormap='Greens').generate(positive_text)
      negative_wc = WordCloud(width=1600, height=800, background_color='white', colormap='Reds').generate(negative_text)
      neutral_wc = WordCloud(width=1600, height=800, background_color='white', colormap='Oranges').generate(neutral_text)
  
  fig3, axs = plt.subplots(1, 3, figsize=(14, 6))
  
  axs[0].imshow(positive_wc, interpolation='bilinear')
  axs[0].axis('off')
  axs[0].set_title('Positive Sentiment Word Cloud')
  
  axs[1].imshow(negative_wc, interpolation='bilinear')
  axs[1].axis('off')
  axs[1].set_title('Negative Sentiment Word Cloud')
  
  axs[2].imshow(neutral_wc, interpolation='bilinear')
  axs[2].axis('off')
  axs[2].set_title('Neutral Sentiment Word Cloud')
  
  fig3.suptitle(f"{selected_restaurant} \nSentiment Analysis - Word Clouds", fontsize=26)
  
  st.pyplot(fig3)
  
  
  st.write("\n # ")
  
  
  overall_sentiment = 'Positive' if positive > max(neutral, negative) else 'Neutral' if neutral > max(positive, negative) else 'Negative'
  
  if overall_sentiment == "Positive":
    sentiment_color = "green"
  elif overall_sentiment == "Neutral":
    sentiment_color = "orange"
  else:
    sentiment_color = "red"
  
  # """
  html_3d_text = f"""
  <div style="text-align: center; background-color: {sentiment_color}; border-radius: 10px; padding: 20px;">
    <h2 style="
        font-family: 'Arial', sans-serif;
        font-size: 50px;
        color: white;  /* Text color */
        text-shadow: 4px 4px 0 rgba(26, 26, 26, 0.5), -2px -2px 0 rgba(26, 26, 26, 0.5), 2px -2px 0 rgba(26, 26, 26, 0.5), -2px 2px 0 rgba(26, 26, 26, 0.5);
    ">
        Overall Sentiment: <strong>{overall_sentiment}</strong>
    </h2>
</div>
    """
  
  st.markdown(html_3d_text, unsafe_allow_html=True)
  
  st.info("""⚠️
          **Food Trend.AI** is a platform developed solely to showcase our thesis. 
          We do not support or condone any actions to promote or demote any restaurants through this platform. Our statistics are based on real data scraped from online 
          food ordering portals. _**The top restaurant rankings presented are derived purely from actual customer ratings and reviews.**_
          \nOur intention is _**not to promote or damage the reputation**_ of any **_restaurants_** or online 
          **_food ordering websites_**. For any clarifications or objections, please contact.
          """)
