#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df_auto_dataset = pd.read_csv('C:/Users/Ayieko/Desktop/python/simplilearn/auto/auto-mpg.csv')


# In[9]:


print(df_auto_dataset)


# In[10]:


df_auto_dataset.head()


# In[12]:


### a user-define function for origin
####### 1-USA, 2-EUROPE, 3-ASIA
def origin(num):
    if num==1:
        return 'USA'
    elif num==2:
        return 'Europe'
    else:
        return 'Asia'
    
## we can use the apply function
df_auto_dataset['origin'] = df_auto_dataset['origin'].apply(origin)


# In[13]:


## view the first 30 data points after applying the user-defined function to the dataset
df_auto_dataset.head(30)


# In[14]:


## draw a pairplot using the sns for mpg, weight, origin, and with hue origin, set size to 4
# note: hue is a variable in the dataset to map plot aspects to different colors
sns.pairplot(df_auto_dataset[['mpg','weight', 'origin']],hue='origin',size=4)


# In[ ]:




