#!/usr/bin/env python
# coding: utf-8

# ### Importing the Libraries

# In[2]:


import pandas as pd #data processing and I/O operations
import numpy as np #Linear Algebra
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly

#!pip install plotly


# ### Import the dataset

# In[3]:


#Import the winter olympics
winter = pd.read_csv('E:/Python/Python - Decodr/DecodR_Class/October - 2021/17-10-2021/In-depth Analysis of Olympic Dataset/winter.csv')
winter.head(10)


# In[3]:


winter.tail(10)


# In[4]:


# Import summer dataset
summer = pd.read_csv("E:/Python/Python - Decodr/DecodR_Class/October - 2021/17-10-2021/In-depth Analysis of Olympic Dataset/summer.csv")
summer.head()


# In[6]:


#Import the dictionary dataset
dict = pd.read_csv('E:/Python/Python - Decodr/DecodR_Class/October - 2021/17-10-2021/In-depth Analysis of Olympic Dataset/dictionary.csv')
dict.head()


# # Analyze the Summer Dataset:

# In[7]:


summer.rename(columns={'Country' : 'Code'}, inplace=True)


# In[7]:


summer.head()


# In[8]:


summer = pd.merge(summer, dict, on='Code', how='outer')


# In[10]:


summer.head()


# In[9]:


summer.describe()


# In[12]:


summer.describe(include=['O'])


# ## Plotting the Choropleth Map

# In[11]:


medals_map = summer.groupby(['Country', 'Code'])['Medal'].count().reset_index()
medals_map = medals_map[medals_map['Medal']>0]


# In[12]:


fig = px.choropleth(medals_map, locations="Code", color='Medal', hover_name='Country',
                   color_continuous_scale=px.colors.sequential.Plasma)

fig.show()


# ### Most successful male athlete 

# In[13]:


print("Most successful male athlete is: ", summer[summer['Gender']=='Men']['Athlete'].value_counts()[:1].index[0],
      'with', summer[summer['Gender']=='Men']['Athlete'].value_counts().values[0], 'medals')


# ### Most successful female athlete

# In[14]:


print("Most successful female athlete is: ", summer[summer['Gender']=='Women']['Athlete'].value_counts()[:1].index[0],
      'with', summer[summer['Gender']=='Women']['Athlete'].value_counts().values[0], 'medals')


# ### Who won the most medals

# In[16]:


medals = summer.groupby(['Athlete', 'Medal'])['Sport'].count().reset_index().sort_values(by='Sport', ascending=False)


# In[17]:


medals


# In[18]:


medals = medals.drop_duplicates(subset=['Medal'], keep='first') 


# In[19]:


medals.columns = [['Athlete', 'Medal', 'Count']]


# In[20]:


medals


# ## Visualize the medal distribution for the top 10 countries

# In[21]:


medals_country = summer.groupby(['Country', 'Medal'])['Gender'].count().reset_index().sort_values(by='Gender', 
                                                                                                  ascending=False)


# In[22]:


medals_country


# In[28]:


medals_country = medals_country.pivot('Country', 'Medal', 'Gender').fillna(0)


# In[25]:


medals_country


# In[26]:


top = medals_country.sort_values(by='Gold', ascending=False)[:10]


# In[27]:


top


# In[28]:


fig = top.plot.barh(width=0.8)
fig = plt.gcf()
fig.set_size_inches(12,12)
plt.title("Medals Distribution in top 10 countries")
plt.show()


# ## Analyze the winter Dataset:

# In[29]:


winter.rename(columns={'Country':'Code'}, inplace=True)


# In[30]:


winter = pd.merge(winter, dict, on='Code', how='outer')


# In[31]:


winter.head()


# In[32]:


winter.describe(include='all')


# In[33]:


winter.describe()


# In[34]:


winter.describe(include='O')


# In[35]:


medals_map = winter.groupby(['Country','Code'])['Medal'].count().reset_index()
medals_map = medals_map[medals_map['Medal']>0]
fig = px.choropleth(medals_map, locations='Code',
                   color='Medal',
                   hover_name='Country',
                   color_continuous_scale=px.colors.sequential.Plasma)

fig.show()


# ### Most successful Male athlete

# In[36]:


print('The most successful male athlete in winter olympics is', 
      winter[winter['Gender'] == 'Men']['Athlete'].value_counts()[:1].index[0], 'with',
     winter[winter['Gender'] == 'Men']['Athlete'].value_counts()[:1].values[0], 'medals')


# ### Most successful female athlete

# In[37]:


print('The most successful female athlete in winter olympics is', 
      winter[winter['Gender'] == 'Women']['Athlete'].value_counts()[:1].index[0], 'with',
     winter[winter['Gender'] == 'Women']['Athlete'].value_counts()[:1].values[0], 'medals')


# ### Medal Distribution in top 10 countries [Winter Olympics]:

# In[38]:


medals_country = winter.groupby(['Country', 'Medal'])['Gender'].count().reset_index().sort_values(by='Gender', ascending=False)


# In[39]:


medals_country


# In[40]:


top = medals_country.pivot('Country', 'Medal', 'Gender').fillna(0)


# In[41]:


top


# In[42]:


top = top.sort_values(by='Gold', ascending=False)[:10]


# In[43]:


top


# In[44]:


fig = top.plot.barh(width=0.8)
fig = plt.gcf()
fig.set_size_inches(12,12)
plt.title('Medals Distribution for top 10 countries [Winter Olympics]')
plt.show()


# In[ ]:




