#!/usr/bin/env python
# coding: utf-8

# # Identifying demographic data
# 
# Demographic data describes who someone is and doesn't change as often as other types of data. When using demographic data to describe a person, caution should be taken to not overgeneralize demographics to other attributes that describe a person such as their behaviors, attitude, or opinions. Demographic data is recorded and tracked when using everyday applications. The value of demographic data is its ability to store insights about (mostly) immutable characteristics of a person

# ## Learning outcomes
# Learners will be able to…
# -	Understand what demographic data is
# -	Identify demographic data attributes
# -	Identify how demographic data is tracked and collected
# -	Use demographic data to describe who someone is
# 

# ## Learner-facing goals
# 
# Let’s learn how demographic data is used to describe who a person is

# ## Lesson plan

# ### Warmup activities
# 
# - List 5-10 things that define who you are
# - List 5-10 things that describe an organization or community you belong to
# - Think of a time you were asked to provide information about yourself (e.g., filling out a form or survey)?
#     - How did it make you feel?
#     - How was the information collected or recorded?

# ### Exercises

# **What demographic data can you find?** Learners view an image, dataset, or graph and find demographic data attributes and values.
# 
# - Select the demographic variables in the dataset:

# In[1]:


import pandas as pd
marketing_campaign = pd.read_csv("datasets/marketing_campaign_data.csv")
marketing_campaign_sml = marketing_campaign[["Year_Birth", " Income ", "Kidhome", "Teenhome", "Dt_Customer", "NumWebPurchases", "NumWebVisitsMonth", "Country"]]
marketing_campaign_sml = marketing_campaign_sml.head()
marketing_campaign_sml["SatisfactionRating"] = [8, 10, 5, 2, 6]
marketing_campaign_sml['Lifestyle'] = ["Foodie", "Outdoor Enthusiast", "Fisherman", "Musician", "Gamer"]
marketing_campaign_sml.columns = ["Year_Birth", "Income", "Kid_at_home", "Teen_at_home", "Sign_up_date", "Web_purchases", "Monthly_web_visits",  "Country", "Satisfaction_rating", "Lifestyle"]
marketing_campaign_sml


# - Select the demographic attributes that describe the image:
# 
# ![millennials](./images/millennials.jpeg)

# **What would happen if things were different?** Learners view a dataset, graph, or image describe how changes would impact the demographic data values being produced or recorded (How mutable is it?)
# 
# - Match the change with the impact to the demographic data in the table:
# 
# Changes
# 1. The person in row 2 has a birthday
# 2. A customer moves from Candada to Germany
# 3. A customer has a bad experience
# 
# Impacts
# 1. No change to the data in the table
# 2. Change their country abbreviation
# 3. A change to satisfaction rating, but this is not a demographic attribute
# 
# - Select and rank the variables in the table from most to least mutable.
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


# **What demographic data will be created?** Learners are provided with a data collection mechanism or scenario and describe the demographic data that will be generated.
# 
# - Match the data collection device with the demographic data being tracked:
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
# - What are 3 things you learned about demographic data?
# - What are 2 things you wonder about demographic data?
# - What is 1 takeaway you could apply to your work, community, or personal life?
# 
# **Going further**
# 
# - Create a table that lists all the demographic data you can find on a historical figure or celebrity you’re interested in knowing more about.
# - Create a table that lists all the population demographics of a country or other geographic region that you live in or are interested in learning more about
# 

# ## Concepts
# 
# -	Demographic data describes who someone is
# -	Demographic data doesn’t change often
# -	When using demographic data to describe a person, caution should be taken to not overgeneralize demographics to other attributes that describe a person such as their behaviors, attitude, or opinions
# -	Demographic data is recorded and tracked when using everyday applications.
# -	The value of demographic data is its ability to store insights about (mostly) immutable characteristics of a person
# 

# ## Keywords
# 
# Demographics, Firmographics, Population demographics, Mutable characteristic, Generalization, Form, Survey, Census, Poll
