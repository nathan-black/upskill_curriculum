#!/usr/bin/env python
# coding: utf-8

# # Identifying behavioral data
# 
# Behavioral data describes a person's actions and is tracked and recorded when you interact with a product or service. When interacting with digital applications, you're behavioral data creates a data trail or digital footprint. The value of behavioral data is its ability to store insights about what people do. An advantage of behavioral data over other forms is that it describes actual actions regardless of who performed those actions or feelings or emotions surrounding the actions.

# ## Learning outcomes
# 
# Learners will be able to…
# -	Understand what behavioral data is
# -	Identify behavioral data attributes
# -	Identify how behavioral data is tracked and collected
# -	Use behavioral data to describe a person's actions

# ## Learner-facing goals
# 
# Let's learn how behavioral data is used to describe what people do

# ## Lesson plan

# ### Warmup activities
# 
# - Describe what you did yesterday
# - Watch [Four Reasons to Care About Your Digital Footprint](https://www.youtube.com/watch?v=Ro_LlRg8rGg)
#     - What are some advantages of having a digital footprint?
#     - What are some drawbacks?
#     - What do you wonder about your digital footprint?

# ### Exercises
# 
# **What behavioral data can you find?** Learners view an image, dataset, or graph and find behavioral data attributes and values.
# 
# - Select the behavioral variables in the dataset:

# In[1]:


import pandas as pd
marketing_campaign = pd.read_csv("datasets/marketing_campaign_data.csv")
marketing_campaign_sml = marketing_campaign[["Year_Birth", " Income ", "Kidhome", "Teenhome", "Dt_Customer", "NumWebPurchases", "NumWebVisitsMonth", "Country"]]
marketing_campaign_sml = marketing_campaign_sml.head()
marketing_campaign_sml["SatisfactionRating"] = [8, 10, 5, 2, 6]
marketing_campaign_sml['Lifestyle'] = ["Foodie", "Outdoor Enthusiast", "Fisherman", "Musician", "Gamer"]
marketing_campaign_sml.columns = ["Year_Birth", "Income", "Kid_at_home", "Teen_at_home", "Sign_up_date", "Web_purchases", "Monthly_web_visits",  "Country", "Satisfaction_rating", "Lifestyle"]
marketing_campaign_sml


# - Select the behavioral attributes that describe the image:
# 
# ![music](./images/listening_to_music.jpeg)

# **What would happen if things were different?** Learners view a dataset, graph, or image describe how changes would impact the behavioral data values being produced or recorded.
# 
# - Match the change with the impact to the behavioral data in the table:
# 
# Changes
# 1. A customer signs up
# 2. A customer quits their job
# 3. A customer makes a purchase on the company website
# 
# Impacts
# 1. A new row is added to the table with a corresponding sign-up date
# 2. Change to income which is a demographic variable not a behavioral variable
# 3. Web_purchases increases by 1 for that customer
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


# **What behavioral data will be created?** Learners are provided with a data collection mechanism or scenario and describe the behavioral data that will be generated.
# 
# - Match the data collection device with the behavioral data being tracked:
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
# - What are 3 things you learned about behavioral data?
# - What are 2 things you wonder about behavioral data?
# - What is 1 takeaway you could apply to your work, community, or personal life?
# 
# **Going further**
# 
# - Create a table that consists of the behavioral data you generate while browsing or shopping online

# ## Concepts
# 
# - Behavioral data describes a person's actions
# - Behavioral data is tracked and recorded when you interact with a product or service
# - When interacting with digital applications, you're behavioral data creates a data trail or digital footprint
# - The value of behavioral data is its ability to store insights about what people do
# - An advantage of behavioral data over other forms is that it describes actual actions regardless of who performed those actions or feelings or emotions surrounding the actions

# ## Keywords
# 
# Behavioral data, digital footprint, data trail, transactional data
