#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# In[4]:


corona_dataset_csv = pd.read_csv("C:/Users/Aashika/Downloads/covid19_deaths_dataset.csv")
corona_dataset_csv.head()


# In[5]:


corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)
corona_dataset_csv.head()


# In[6]:


corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
corona_dataset_aggregated.head()


# In[10]:


corona_dataset_aggregated.loc["China"][:100].plot()
corona_dataset_aggregated.loc["US"][:100].plot()
corona_dataset_aggregated.loc["India"][:100].plot()
plt.legend()


# In[11]:


countries = list(corona_dataset_aggregated.index)
max_death_rate = []
for c in countries :
    max_death_rate.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["max_death_rate"] = max_death_rate


# In[12]:


corona_dataset_aggregated.head()


# In[13]:


corona_data = pd.DataFrame(corona_dataset_aggregated["max_death_rate"])
corona_data.head()


# In[14]:


happiness_report_csv = pd.read_csv("C:/Users/Aashika/Downloads/worldwide_happiness_report.csv")
happiness_report_csv.head()


# In[15]:


happiness_report_csv.shape


# In[16]:


happiness_report_csv.drop(["Overall rank","Score","Generosity","Perceptions of corruption"],axis=1, inplace=True)
happiness_report_csv.head()


# In[17]:


happiness_report_csv.shape


# In[18]:


happiness_report_csv.set_index("Country or region",inplace=True)
happiness_report_csv.head()


# In[19]:


data = corona_data.join(happiness_report_csv,how="inner")
data.head()


# In[20]:


data.corr()


# In[26]:


np.seterr(divide = 'ignore')


# In[27]:


x = data["GDP per capita"]
y = data["max_death_rate"]
sns.scatterplot(x,np.log(y))


# In[32]:


sns.regplot(x,y)


# In[33]:


x = data["Social support"]
y = data["max_death_rate"]
sns.scatterplot(x,np.log(y))


# In[34]:


sns.regplot(x,y)


# In[35]:


x = data["Healthy life expectancy"]
y = data["max_death_rate"]
sns.scatterplot(x,np.log(y))


# In[36]:


sns.regplot(x,y)


# In[37]:


x = data["Freedom to make life choices"]
y = data["max_death_rate"]
sns.scatterplot(x,np.log(y))


# In[38]:


sns.regplot(x,y)

