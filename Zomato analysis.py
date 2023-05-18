#!/usr/bin/env python
# coding: utf-8

# # Zomato dataset EDA

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv('zomato.csv', encoding = 'latin-1')
df.head()


# In[5]:


df.columns


# In[29]:


df.info()


# In[7]:


df.describe()


# ## in data analytics what all things to do
# 1. missing values
# 2. explore about the numerical variables
# 3. explore about categorical variables
# 4. finding realtionship between features

# In[9]:


df.isnull().sum()


# In[10]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[12]:


sns.heatmap(df.isnull(), yticklabels = False, cbar = False, cmap = 'viridis')


# In[13]:


df_country = pd.read_excel('Country-code.xlsx')
df_country.head()


# In[14]:


df.columns


# In[17]:


# COMBINE THE Dataset

final_df = pd.merge(df, df_country, on = 'Country Code', how = 'left')


# In[18]:


final_df.head(2)


# In[21]:


## To check the datatypes
final_df.dtypes


# In[23]:


country_names = final_df.Country.value_counts().index


# In[25]:


country_val = final_df.Country.value_counts().values


# In[30]:


## Pie chart - top 3 country that use zomato
plt.pie(country_val[:3], labels = country_names[:3], autopct = '%1.2f%%')


# Observation:zomato maximum records or transcation from india after that usa and then uk

# In[35]:


ratings = final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns = {0:'Rating Count'})


# In[37]:


ratings


# # Observations
# 
# 1. When rating is between 4.5 to 4.9 is Excellent
# 2. When rating is between 4.0 to 4.4 is very good
# 3. When rating is between 3.5 to 3.9 is good
# 4. When rating is between 3.0 to 3.4 is average
# 5. when rating is between 2.5 to 2.9 is average
# 6. When rating is between 2.0 to 2.4 is poor

# In[38]:


ratings.head()


# In[ ]:





# In[44]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="Aggregate rating", y="Rating Count",data=ratings)


# In[46]:


sns.barplot(x="Aggregate rating", y="Rating Count", hue="Rating color",data=ratings, palette=['white', 'red', 'orange', 'yellow', 'green', 'green'])


# ## Obseravations
# 1. not rated count is verye high
# 2. maximum no of ratings are between 2.5 to 3.4
# 

# In[47]:


## Count plot
sns.countplot(x = "Rating color", data = ratings, palette = ['white', 'red', 'orange', 'yellow', 'green', 'green'])


# In[48]:


ratings


# In[56]:


### Find the countries name that has given 0 rating
final_df[final_df['Rating color'] == 'White'].groupby(['Aggregate rating', 'Country']).size().reset_index().head(5)


# In[57]:


## find out which currency is used by which country
final_df.columns


# In[58]:


final_df[final_df.['Has Online delivery']


# In[61]:


## which country do have online deliveries option
final_df[final_df['Has Online delivery'] == "Yes"].Country.value_counts()


# In[62]:


final_df[['Has Online delivery', 'Country']].groupby(['Has Online delivery', 'Country']).size().reset_index()


# Observations:
#     1. online deliveries are available in india and UAE

# In[ ]:


## create apie chart for top 5 cities distribution


# In[64]:


final_df.City.value_counts().index


# In[71]:


city_values = final_df.City.value_counts().values
city_labels = final_df.City.value_counts().index


# In[72]:


plt.pie(city_values[:5], labels = city_labels[:5])


# In[ ]:


8

