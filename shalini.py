#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas-profiling')


# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns 
import os
import ydata_profiling 


# In[4]:


pd.read_excel("C:/Users/91951/Downloads/Event Registration (Responses).xlsx")


# In[5]:


df= pd.read_excel("C:/Users/91951/Downloads/Event Registration (Responses).xlsx")


# In[6]:


df.head()


# In[8]:


df.profile_report()


# In[ ]:




