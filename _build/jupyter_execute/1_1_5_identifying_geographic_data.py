#!/usr/bin/env python
# coding: utf-8

# # Identifying geographic data

# ## Learning outcomes
# 
# Learners will be able to…
# -	Understand what geographic data is
# -	Identify geographic data attributes
# -	Identify how geographic data is tracked and collected
# -	Use geographic data to describe location, movement, climate, and culture

# ## Learner-facing goals
# 
# Let's learn how to use geographic data to describe where something or someone is, where it is (or they are) going, and the climate and culture associated with a place.

# ## Lesson plan

# ### Warmup activities
# 
# - Read the quote and answer the questions that follow:
#     - Does it surprise you to know that your location is being tracked?
#     
# *At least 75 companies receive anonymous, precise location data from apps whose users enable location services to get local news and weather or other information, The Times found. Several of those businesses claim to track up to 200 million mobile devices in the United States — about half those in use last year. The database reviewed by The Times — a sample of information gathered in 2017 and held by one company — reveals people’s travels in startling detail, accurate to within a few yards and in some cases updated more than 14,000 times a day.*
# 
# - List 3-5 things that location data could reveal about you.

# ### Exercises
# 
# **What geographic data can you find?** Learners view an image, dataset, or graph and find geographic data attributes and values.
# 
# - Select the geographic variables in the dataset:

# In[1]:


import pandas as pd
marketing_campaign = pd.read_csv("datasets/marketing_campaign_data.csv")
marketing_campaign_sml = marketing_campaign[["Year_Birth", " Income ", "Kidhome", "Teenhome", "Dt_Customer", "NumWebPurchases", "NumWebVisitsMonth", "Country"]]
marketing_campaign_sml = marketing_campaign_sml.head()
marketing_campaign_sml["SatisfactionRating"] = [8, 10, 5, 2, 6]
marketing_campaign_sml['Lifestyle'] = ["Foodie", "Outdoor Enthusiast", "Fisherman", "Musician", "Gamer"]
marketing_campaign_sml.columns = ["Year_Birth", "Income", "Kid_at_home", "Teen_at_home", "Sign_up_date", "Web_purchases", "Monthly_web_visits",  "Country", "Satisfaction_rating", "Lifestyle"]
marketing_campaign_sml


# - Select the geographic attributes that describe the image:

# **What would happen if things were different?** Learners view a dataset, graph, or image describe how changes would impact the geographic data values being produced or recorded.
# 
# - Match the change with the impact to the geographic data in the table:
# 
# Changes
# 1. A customer moves
# 2. A person visits the website while on vacation
# 3. A person calls customer service to correct their year of birth
# 
# Impacts
# 1. This may impact the Country field if the move is outside the country they currently live in
# 2. This does not impact the current table, but would likely impact location data recorded for the visit
# 3. This would impact Year_Birth, but this is a temporal attribute, not a geographic attribute

# In[2]:


import pandas as pd
marketing_campaign = pd.read_csv("datasets/marketing_campaign_data.csv")
marketing_campaign_sml = marketing_campaign[["Year_Birth", " Income ", "Kidhome", "Teenhome", "Dt_Customer", "NumWebPurchases", "NumWebVisitsMonth", "Country"]]
marketing_campaign_sml = marketing_campaign_sml.head()
marketing_campaign_sml["SatisfactionRating"] = [8, 10, 5, 2, 6]
marketing_campaign_sml['Lifestyle'] = ["Foodie", "Outdoor Enthusiast", "Fisherman", "Musician", "Gamer"]
marketing_campaign_sml.columns = ["Year_Birth", "Income", "Kid_at_home", "Teen_at_home", "Sign_up_date", "Web_purchases", "Monthly_web_visits",  "Country", "Satisfaction_rating", "Lifestyle"]
marketing_campaign_sml


# **What geographic data will be created?** Learners are provided with a data collection mechanism or scenario and describe the geographic data that will be generated.
# 
# - Match the data collection device with the geographic data being tracked:
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
# - What are 3 things you learned about geographic data?
# - What are 2 things you wonder about geographic data?
# - What is 1 takeaway you could apply to your work, community, or personal life?
# 
# **Going further**
# 
# - Create a table that consists of the geoographic data that describes where you were and where you went yesterday

# ## Concepts
# 
# - Geographic data describes 

# ## Keywords
