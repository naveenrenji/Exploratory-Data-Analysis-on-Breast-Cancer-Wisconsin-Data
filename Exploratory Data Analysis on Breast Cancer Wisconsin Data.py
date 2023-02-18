#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


# ## Load the dataset

# In[2]:


df = pd.read_csv("breast-cancer-wisconsin.csv")


# In[3]:


df.head()


# In[4]:


num_rows = df.shape[0]
print(num_rows)


# ## Summarizing each column (e.g. min, max, mean )

# In[5]:


df = df.replace('?', float('nan'))
df["F6"] = pd.to_numeric(df["F6"])
df.describe()


# In[6]:


print(df['F2'].describe(include='all'))


# In[7]:


print(df['F3'].describe(include='all'))


# In[8]:


print(df['F4'].describe(include='all'))


# In[9]:


print(df['F5'].describe(include='all'))


# In[10]:


df = df.replace('?', float('nan'))
df["F6"] = pd.to_numeric(df["F6"])
print(df['F6'].describe(include='all'))


# In[11]:


print(df['F7'].describe(include='all'))


# In[12]:


print(df['F8'].describe(include='all'))


# In[13]:


print(df['F9'].describe(include='all'))


# In[14]:


print(df['Class'].describe(include='all'))


# ## Identify missing values
# 

# In[15]:


print(df.isnull().sum())


# ## Replacing the missing values with the “mean” of the column

# In[16]:


#Finding the mean of the column having NaN
mean_value=df['F6'].mean()
  
# Replace NaNs in column F6 with the
# mean of values in the same column
df['F6'].fillna(value=mean_value, inplace=True)
print(df.isnull().sum())


# ## Displaying the frequency table of “Class” vs. F6

# In[17]:


df.value_counts(['Class', 'F6']).reset_index().rename(columns={0:'count'})


# ## Displaying the scatter plot of F1 to F6, one pair at a time

# In[18]:


columns = ['F1', 'F2',
            'F3','F4','F5','F6']
   
scatter_matrix(df[columns])
plt.show()


# ##  Box plot for columns F7 to F9

# In[19]:


df.iloc[:, 7:10].plot(kind='box', subplots=True, layout=(1, 3), sharex=False)
plt.show()


# ##  Histogram plot for columns F7 to F9

# In[20]:


df.iloc[:, 7:10].hist()
plt.show()


# ## Delete all the objects from the environment. Reload the “breast-cancer-wisconsin.data.csv” from 
# canvas into R. Remove any row with a missing value in any of the columns.

# In[21]:


get_ipython().run_line_magic('reset', '-f')


# ## Reload the “breast-cancer-wisconsin.data.csv”

# In[22]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

df = pd.read_csv("breast-cancer-wisconsin.csv")


# In[23]:


df = df.replace('?', float('nan'))
df["F6"] = pd.to_numeric(df["F6"])
num_rows = df.shape[0]
print(num_rows)


# In[24]:


print(df.isnull().sum())


# In[25]:


df.dropna(how="any", inplace=True)


num_rows = df.shape[0]
print(num_rows)


# In[26]:


df.describe()


# In[ ]:




