#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib')


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import numpy as np

xpts = np.array([0,4])
ypts = np.array([0,100])
plt.plot(xpts, ypts)
plt.show()


# In[ ]:




