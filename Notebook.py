#!/usr/bin/env python
# coding: utf-8

# In[127]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[128]:


df = pd.read_csv(r"C:\Users\abdin\Desktop\WIP\Data\WB_PIP.csv")
df.head(20)


# In[129]:


df.columns


# In[130]:


df.info


# In[131]:


df.isna().sum()


# In[132]:


df["INDICATOR"].value_counts


# In[133]:


poverty = df[df["INDICATOR"] == 'WB_PIP_HEADCOUNT_IPL']


# In[134]:


poverty[['REF_AREA_LABEL','TIME_PERIOD','OBS_VALUE']].head()


# In[135]:


poverty.duplicated(subset=['REF_AREA_LABEL','TIME_PERIOD']).sum()


# In[136]:


poverty["AGE_LABEL"].value_counts()
poverty["SEX_LABEL"].value_counts()
poverty["URBANISATION_LABEL"].value_counts()


# In[137]:


poverty["URBANISATION_LABEL"].unique()


# In[138]:


poverty_total = poverty[poverty["URBANISATION_LABEL"] == "Total"].copy()


# In[139]:


poverty_total.duplicated(subset=["REF_AREA_LABEL","TIME_PERIOD"]).sum()


# In[140]:


poverty_total["OBS_VALUE"].astype
poverty_total["OBS_VALUE"].dtype


# In[141]:


poverty_total["OBS_VALUE"].describe()


# In[142]:


poverty_total["TIME_PERIOD"] = pd.to_datetime(poverty_total["TIME_PERIOD"], format = '%Y')


# In[143]:


poverty_total["TIME_PERIOD"].dtype


# In[144]:


poverty_total.groupby(['REF_AREA_LABEL','TIME_PERIOD']).size().max()


# In[145]:


poverty_total["SEX_LABEL"].value_counts()


# In[146]:


poverty_total["AGE_LABEL"].value_counts()


# In[147]:


poverty_total.groupby(['REF_AREA_LABEL','TIME_PERIOD']).size().sort_values(ascending=False).head()


# In[148]:


example = poverty_total[
    (poverty_total['REF_AREA_LABEL'] == 'Hungary') &
    (poverty_total['TIME_PERIOD'] == pd.Timestamp('1999-01-01'))
]

example


# In[149]:


example[['OBS_VALUE','OBS_STATUS_LABEL','OBS_CONF_LABEL','DATABASE_ID']]


# In[152]:


poverty_clean = (
    poverty_total
    .groupby(['REF_AREA_LABEL','TIME_PERIOD'], as_index = False)['OBS_VALUE']
    .mean()
)


# In[153]:


poverty_clean.groupby(['REF_AREA_LABEL','TIME_PERIOD']).size().max()


# In[154]:


poverty_clean['year']= poverty_clean['TIME_PERIOD'].dt.year


# In[156]:


poverty_clean = poverty_clean[['REF_AREA_LABEL','year','OBS_VALUE']]


# In[158]:


poverty_clean = poverty_clean[['REF_AREA_LABEL','year','OBS_VALUE']]


# In[162]:


poverty_clean.columns = ['country','year','poverty_rate']
poverty_clean.head()


# In[167]:


Kenya = poverty_clean[poverty_clean['country'] == 'Kenya']
Kenya.sort_values('year')


# In[168]:


Kenya['poverty_rate'].iloc[-1] - Kenya['poverty_rate'].iloc[0]


# In[169]:


Kenya[Kenya['year'] < 2000]['poverty_rate'].mean()


# In[170]:


Kenya[Kenya['year'] >= 2010]['poverty_rate'].mean()


# In[173]:


import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.plot(Kenya['year'], Kenya['poverty_rate'])
plt.xlabel('Year')
plt.ylabel('Poverty Rate (%)')
plt.title('Kenya Poverty Trend')
plt.show()


# In[174]:


Kenya['poverty_rate'].std()


# Kenya does not exhibit a steady poverty trend. It exhibits shock sensitivity. Welfare improvements are not persistent, and gains reverse after adverse conditions.!!
