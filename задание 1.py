#!/usr/bin/env python
# coding: utf-8

# In[13]:


get_ipython().system('pip install pandas')
import pandas as pd
dataset = pd.read_csv('try1.csv',sep=';')
dataset.head(13669)


# In[14]:


dataset['TIME'] = pd.to_datetime(dataset['TIME'])


# In[15]:


dataset['YEAR_MONTH'] = dataset['TIME'].dt.to_period('M')


# In[16]:


result = dataset.groupby(['BANK_ID', 'YEAR_MONTH']).agg(
    total_turnover=('AMOUNT', 'sum'),
    operation_count=('TRANSACTION_ID', 'count')
).reset_index()


# In[17]:


result['YEAR_MONTH'] = result['YEAR_MONTH'].astype(str)


# In[18]:


result = result.sort_values(by=['BANK_ID', 'YEAR_MONTH'])


# In[19]:


print(result)


# In[ ]:




