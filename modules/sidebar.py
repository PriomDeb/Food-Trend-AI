import streamlit as st

def sidebar():
    thesis_details = st.sidebar.expander("✒️ Thesis Details")
    with thesis_details:
        thesis_details.info("""
                            #### Title
                             
                            Sentiment Analysis of Customer Reviews on Food Ordering Portals of Bangladesh using Natural Language Processing
                            """)
        thesis_details.success("""
                    #### Abstract 
                    In recent years, the popularity of online food ordering services has surged, offering consumers a convenient way to 
                    order food from restaurants and have it delivered to their doorstep. During this period, HungryNaki and Foodpanda Bangladesh have been identified as key 
                    contributors to the growth and advancement of the online food delivery market. This study aims to anticipate the 
                    sentiments of Bangladeshi customers towards online meal ordering services, with a specific focus on Foodpanda Bangladesh and HungryNaki. 
                    We created a new dataset for this research, subjected it to preprocessing and employed six machine learning models and three deep neural network models. 
                    In the machine learning approach, the Random Forest Classifier demonstrated excellence in accuracy, precision, and recall, achieving an accuracy rate of 80.31%. 
                    On the other hand, the BERT Classifier performed effectively in the deep learning approach, boasting an accuracy of 89%. 
                    Despite challenges such as data ambiguity and imbalances in the dataset, our findings underscore the potential of the BERT model in sentiment analysis, 
                    offering valuable insights for future research in this field.
                    """)
        
    authors = st.sidebar.expander("👨‍💻 Authors ", expanded=True)
    with authors:
        authors.success("""
                        - Priom Deb
                        - Asibur Rahman Bhuiyan
                        - Farhan Ahmed
                        - Rakib Hassan
                        - Habiba Mahrin
                        - Faisal Ahmed
                        - Dewan Ziaul Karim
                        """)
    
    st.sidebar.warning("""
                       **Disclaimer:**
                       The dataset used in our platform, **Food Trend.AI**, consists of customer food reviews collected from online 
                       food ordering portals in Bangladesh. These reviews were publicly accessible and viewable by both 
                       users and visitors of the websites, even without logging in. Prior to initiating the 
                       scraping process, we thoroughly reviewed the terms and conditions of these 
                       websites to ensure compliance with their policies regarding the scraping and usage of publicly viewable customer reviews. 
                       We found no restrictions or prohibitions against scraping and using this data.
                       
                       The dataset has been utilized for our thesis on sentiment analysis. We have not altered any data within the 
                       dataset; all reviews are genuine. For text processing, we only removed unwanted punctuations to clean the text for our model training.
                       
                       **Food Trend.AI** is a platform developed solely to showcase our thesis. 
                       We do not support or condone any actions to promote or demote any restaurants through this platform. Our statistics are based on real data scraped from online 
                       food ordering portals. _**The top restaurant rankings presented are derived purely from actual customer ratings and reviews.**_
                       
                       Our intention is _**not to promote or damage the reputation**_ of any **_restaurants_** or online 
                       **_food ordering websites_**. For any clarifications or objections, please contact.

                       """)
        

        

