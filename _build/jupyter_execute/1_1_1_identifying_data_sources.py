#!/usr/bin/env python
# coding: utf-8

# # Identifying data sources
# Data is used to describe real-world objects and events. Observations are described by their attributes which store data values or specific measurements for each observation. Data values vary across observations. Data is created by processes and applications in professional, public, and personal domains. Data is tracked and recorded to support business operations, public services, and personal applications. The value of data goes beyond a supporting role to providing insights about the thing or event it describes.

# ## Learning outcomes
# After completing this lesson, learners will be able to...
# - Understand what data is
# - Demonstrate an awareness of where data comes from in professional, public, and personal domains
# - Identify how data is tracked and collected
# - Identify observations, attributes, and variables
# - Use data to describe people, places, objects, and actions

# ## Learner-facing goals
# Let’s learn what data is, where it comes from and how you can use it to describe people, places, objects, and actions

# ## Lesson plan

# ### Warmup activities
# 
# - When have you felt like a device (e.g., your smartphone, TV, or favorite website) were tracking you?
# - Read the quote and answer the questions that follow:
#     - What does this quote make you wonder?
#     - How does this quote make you feel?
# 
# *There were 5 exabytes of information created between the dawn of civilization through 2003, but that much information is now created every two days.* Eric Schmidt, Executive Chairman at Google https://careerfoundry.com/en/blog/data-analytics/inspirational-data-quotes/
# 
# 
# - Create a data source concept map:
#     - List up to 5 places you’ve seen data in your work, community, or personal life
#     - Where do you think each of those data sets came from? What process or event produced the data?
# - Watch the [Target video](https://www.youtube.com/watch?v=XvSA-6BJkx4&feature=youtu.be)
#     - How do you think Target knew the daughter was pregnant before her father did?
# 

# ### Exercises

# **What data can you find?** Learners view an image, dataset, or graph and find data observations, attributes, and values.

# - View the table and answer the questions that follow:
#     - What observations are described in the table?
#     - What attributes describe the observations in the table?
#     - What data value describes the satisfaction rating for EmpID 10084?

# In[1]:


import pandas as pd
hr = pd.read_csv("datasets/HRDataset.csv")
to_keep = ["EmpID", "EmpStatusID", "Salary", "Position", "DOB", "DateofHire", "EmpSatisfaction"]
hr = hr[to_keep]
hr.head(5)


# - Fill in the missing data attributes and values in the table to describe the image:

# ![music](./images/listening_to_music.jpeg)

# ![musictable](./images/listening_to_music_table.png)

# - Create a table with attributes, observations, and data values that describe the graph:
# 
# ![jobgrowth](./images/job_growth_stacked_bar_chart.png)
# 
# 

# ![blanktable](./images/blank_table.png)

# **Where is this type of data found?** Learners view a dataset or graph and categorize the domain as professional, public, personal, or undefined

# - View the data table and answer the questions that follow:
#     - What domain does the data displayed in the table belong to?

# In[2]:


import pandas as pd
run = pd.read_csv("datasets/running_metrics.csv")
to_keep = ['event_id', 'total_running_time', 'total_dist', 'rest_time', 'avg_hr', 'avg_speed', 'avg_alt']
run = run[to_keep]
run.columns = ['event_id', 'total_running_time', 'total_distance', 'rest_time', 'avg_heart_rate', 'avg_speed', 'avg_altitude']
run['total_running_time'] = round(run['total_running_time'], 1)
run['total_distance'] = round(run['total_distance'], 1)
run['rest_time'] = round(run['rest_time'], 1)
run['avg_heart_rate'] = round(run['avg_heart_rate'], 1)
run['avg_speed'] = round(run['avg_speed'], 1)
run['avg_altitude'] = round(run['avg_altitude'], 1)
run.head()


# - View the graph and answer the questions that follow:
#     - What domain does the data displayed in the chart belong to?

# ![seattle](./images/SeattleHomelessnessBarChart.png)

# - View the data table and answer the questions that follow:
#     - What domain does the data in the table belong to?

# In[3]:


import pandas as pd
game = pd.read_csv("datasets/video_games_sales_2016.csv")
game.head().T


# Match the data to its domain - TODO

# **What would happen if things were different?** Learners view a dataset, graph, or image describe how changes would impact the data values being produced or recorded.

# - Match the change with the impact to the data in the table:
# 
# Changes
# 1. Salary increases for employee 10069
# 2. Hire a new employee
# 3. Track weekly hours
# 
# Impacts
# 1. Add an observation to the table
# 2. Change a data value in the table
# 3. Add an attribute to the table
# 
# 
# - Which observations have Salary values that vary from employee 100196?
# - Which employees have the same date of hire?

# In[4]:


import pandas as pd
hr = pd.read_csv("datasets/HRDataset.csv")
to_keep = ["EmpID", "EmpStatusID", "Salary", "Position", "DOB", "DateofHire", "EmpSatisfaction"]
hr = hr[to_keep]
hr.head(5)


# **What data will be created?** Learners are provided with a data collection mechanism or scenario and describe the data that will be generated.

# - Match the data collection device with the data being tracked:
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
# - What are 3 things you learned about identifying data sources?
# - What are 2 things you wonder about?
# - What is 1 takeaway you could apply to your work, community, or personal life?
# 
# **Going further**
# 
# Create a data table that describes something you're interested in. Feel free to use the ideas below or come up with your own:
# - Favorite songs
# - The weather
# - A recent shopping trip

# ## Concepts
# -	People, things, and actions can be described using data
# -	More than just numbers, data includes text, images, locations, sounds, and time
# -	Observations are objects or events whose characteristics can be described by attributes or measurements.
# -	Specific measurements are recorded as data values
# -	Data can vary from one observation to the next
# -	Data is used to describe objects and things that happen in professional, public, and personal domains
# -	Data is more than an abstract idea; it records real-life things or events. When you come across data, it is important to remember that it is typically describing things that exist or things that occurred in the real world
# -	Data values vary across individual observations. A difference in a measurement describing an object or event will result in a difference in the data value that is recorded
# -	Data is recorded and tracked by everyday devices.
# -	Data is often generated as a byproduct of business operations, public services, or personal applications, but the value of data is its ability to store insights about the processes that created it

# ## Keywords
# 
# Data, Observation, Attribute, Data value, Variable, Internet of Things (IoT), Quantified self, Open data, Data trail, Digital footprint

# In[ ]:




