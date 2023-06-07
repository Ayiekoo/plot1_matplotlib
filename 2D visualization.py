#!/usr/bin/env python
# coding: utf-8

# In[4]:


### A nutri world-wide firm wants to know how many people visits its website in a particular time. This analysis helps it control and monitor the website traffic
### 2D plot

import matplotlib.pyplot as plt
from matplotlib import style
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


"""
Website traffic data
Number of users or visitors on the website
"""
web_customers = [123,645,950,1290,1630,1450,1034,1295,465,205,80]
time_hr = [7,7,9,10,11,12,13,14,15,16,17]


# In[7]:


#### select style
style.use('ggplot')
### plot the website traffic data (X-axis hrs and Y-axis web customers)
plt.plot(time_hr,web_customers)
### set the title for the plot
plt.title('Web site traffic')
### set the label for the x axis
plt.xlabel('Hrs')
## set label for y axis
plt.ylabel('Number of users')
plt.show()


# In[12]:


#### select style
style.use('ggplot')
### plot the website traffic data (X-axis hrs and Y-axis web customers)
plt.plot(time_hr,web_customers,color = 'y',linestyle = '--', linewidth=2.5)
### set the title for the plot
plt.title('Web site traffic')
### set the label for the x axis
plt.xlabel('Hrs')
## set label for y axis
plt.ylabel('Number of users')
plt.show()


# In[14]:


#### select style
style.use('ggplot')
### plot the website traffic data (X-axis hrs and Y-axis web customers)
plt.plot(time_hr,web_customers,alpha=.4)
### set the title for the plot
plt.title('Web site traffic')
### anottaing the graph
plt.annotate('Max',ha='center',va='bottom',xytext=(8,1500),xy=(11,1630),arrowprops = { 'facecolor' : 'green'})
### set the label for the x axis
plt.xlabel('Hrs')
## set label for y axis
plt.ylabel('Number of users')
plt.show()


# In[33]:


### website traffic data
### number of users or visitors on the website
# monday web traffic
thur = [123,645,950,1290,1630,1450,1034,1295,465,205,80]
# tuesday web traffic
tuesday = [95,680,889,1145,1670,1323,1119,1265,510,310,110]
# wednesday web traffic
wednesday = [105,630,700,1006,1520,1124,1239,1380,580,610,230]
## time distribution
time_hrs = [7,8,9,10,11,12,13,14,15,16,17]


# In[36]:


## select the style of the plot
style.use('ggplot')
#### plot the website traffic data (X-axis hrs and Y-axis as number of users)
#### plot the monday web traffic with red color
plt.plot(time_hrs,thur,'r',label='thur',linewidth=1)
### plot the monday web traffic with green color
plt.plot(time_hrs,tuesday,'g',label='tuesday',linewidth=1.5)
##### plot the monday web traffic with blue color
plt.plot(time_hrs,wednesday,'b',label='wednesday',linewidth=2)
plt.axis([6.5,17.5,50,2000])
### set the title of the plot
plt.title('Web site traffic')
## set label for x axis
plt.xlabel('Hrs')
## set label for y axis
plt.ylabel('Number of users')
plt.legend()
plt.show()


# In[35]:





# In[ ]:




