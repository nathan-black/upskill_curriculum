#!/usr/bin/env python
# coding: utf-8

# # Identifying psychographic data
# 
# Psychographic data describes a person's lifestyle, interests, opinions, beliefs, affiliations, personality, values, emotion, and preferences. This type of data is tracked and recorded when you express your opinions, personality, or preferences through ratings and reviews, surveys, or your lifestyle. Pyschographic data can be inferred from data about what you do and where you go. The value of psychographic is its ability to store insights into what motivates a person's actions

# ## Learning outcomes
# 
# Learners will be able to…
# -	Understand what psychographic data is
# -	Identify psychographic data attributes
# -	Identify how psychographic data is tracked and collected
# -	Use psychographic data to describe a person's attitudes, opinions, and personality

# ## Learner-facing goals
# 
# Let's learn how to use psychographic data to describe people's attitudes, opinions, and personality.

# ## Lesson plan

# ### Warmup activities
# 
# - Read the quote and answer the questions that follow:
#     - Have you ever taken a personality test? Was it for work, fun, or some other purpose?
#     - How do you feel about companies using personality traits to evaluate job candidates?
# 
# *As many as 60 percent of workers are now asked to take workplace assessments. The $500-million-a-year industry has grown by about 10 percent annually in recent years. While many organizations use personality testing for career development, about 22 percent use it to evaluate job candidates, according to the results of a 2014 survey of 344 Society for Human Resource Management members.* - https://www.shrm.org/hr-today/news/hr-magazine/pages/0615-personality-tests.aspx
# 
# - List 3-5 things that describe your personality, opinions, beliefs, or attitude.

# ### Exercises
# 
# **What psychographic data can you find?** Learners view an image, dataset, or graph and find psychographic data attributes and values.
# 
# - Select the psychographic variables in the dataset:

# In[1]:


import pandas as pd
marketing_campaign = pd.read_csv("datasets/marketing_campaign_data.csv")
marketing_campaign_sml = marketing_campaign[["Year_Birth", " Income ", "Kidhome", "Teenhome", "Dt_Customer", "NumWebPurchases", "NumWebVisitsMonth", "Country"]]
marketing_campaign_sml = marketing_campaign_sml.head()
marketing_campaign_sml["SatisfactionRating"] = [8, 10, 5, 2, 6]
marketing_campaign_sml['Lifestyle'] = ["Foodie", "Outdoor Enthusiast", "Fisherman", "Musician", "Gamer"]
marketing_campaign_sml.columns = ["Year_Birth", "Income", "Kid_at_home", "Teen_at_home", "Sign_up_date", "Web_purchases", "Monthly_web_visits",  "Country", "Satisfaction_rating", "Lifestyle"]
marketing_campaign_sml


# - Select the psychographic attributes that describe the image:
# 
# ![music](./images/listening_to_music.jpeg)

# **What would happen if things were different?** Learners view a dataset, graph, or image describe how changes would impact the psychographic data values being produced or recorded.
# 
# - Match the change with the impact to the psychographic data in the table:
# 
# Changes
# 1. A customer visits the website
# 2. A customer has a bad experience and fills out a satisfaction survey
# 3. A customer changes hobbies
# 
# Impacts
# 1. Monthly_web_visits would increase, but this is a behavioral variable, not a psychographic variable
# 2. Satisfaction_rating would decrease and likely impact web visit and/or purchases
# 3. Lifestyle would change
# 

# In[2]:


import pandas as pd
marketing_campaign = pd.read_csv("datasets/marketing_campaign_data.csv")
marketing_campaign_sml = marketing_campaign[["Year_Birth", " Income ", "Kidhome", "Teenhome", "Dt_Customer", "NumWebPurchases", "NumWebVisitsMonth", "Country"]]
marketing_campaign_sml = marketing_campaign_sml.head()
marketing_campaign_sml["SatisfactionRating"] = [8, 10, 5, 2, 6]
marketing_campaign_sml['Lifestyle'] = ["Foodie", "Outdoor Enthusiast", "Fisherman", "Musician", "Gamer"]
marketing_campaign_sml.columns = ["Year_Birth", "Income", "Kid_at_home", "Teen_at_home", "Sign_up_date", "Web_purchases", "Monthly_web_visits",  "Country", "Satisfaction_rating", "Lifestyle"]
marketing_campaign_sml


# **What psychographic data will be created?** Learners are provided with a data collection mechanism or scenario and describe the psychographic data that will be generated.
# 
# - Match the data collection device with the psychographic data being tracked:
# 
# 1. Sensor on a coffee maker
# 2. Traffic camera
# 3. Customer Relationship Management(CRM) system
# 4. Fitness wristwatch
# 5. Political poll
# 6. Ecommerce website

# ### Wrap-up
# 
# **3-2-1 Prompt**
# - What are 3 things you learned about psychographic data?
# - What are 2 things you wonder about psychographic data?
# - What is 1 takeaway you could apply to your work, community, or personal life?
# 
# **Going further**
# 
# - Create a table that consists of the psychographic data that describes your food preferences.

# ## Concepts
# 
# - Psychographic data describes a person's lifestyle, interests, opinions, beliefs, affiliations, personality, values, emotion, and preferences
# - Psychographic data is tracked and recorded when you express your opinions, personality, or preferences through ratings and reviews, surveys, or your lifestyle
# - Pyschographic data can be inferred from data about what you do and where you go
# - The value of psychographic is its ability to store insights into what motivates a person's actions

# ## Keywords
# 
# Psychographic data, personality traits, personality test, opinion poll

# In[ ]:




