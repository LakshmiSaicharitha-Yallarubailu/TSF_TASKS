#!/usr/bin/env python
# coding: utf-8

# # THE SPARKS FOUNDATION
# NAME: Y.LAKSHMI SAICHARITHA
# 

# # 1.Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’ 2.As a business manager, try to find out the weak areas where you can work to make more profit.

# In[34]:


#Importing the libraries
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


# In[2]:


#loading dataset
ds=pd.read_csv(r"C:\Users\Saicharitha\Downloads\SampleSuperstore.csv")
ds


# In[3]:


ds.head(6)


# In[4]:


ds.tail(3)


# In[5]:


ds.info()


# In[6]:


ds.describe()


# In[7]:


ds.isnull().sum()


# In[8]:


ds.isna().sum()


# In[9]:


ds.drop(['Postal Code'],axis=1,inplace=True)


# In[10]:


ds


# In[11]:


sales_ds = ds.groupby('Category', as_index=False)['Sales'].sum()
subcat_ds = ds.groupby(['Category','Sub-Category'])['Sales'].sum()
subcat_ds['Sales']=map(int,subcat_ds)
sales_ds


# # Exploratory Data Analysis

# In[12]:


ds.plot(x='Quantity',y='Sales',style='.')
plt.title('Quantity vs Sales')
plt.xlabel('Quantity')
plt.ylabel('Sales')
plt.grid()
plt.show()


# In[13]:


ds.plot(x='Discount',y='Profit',style='.')
plt.title('Discount vs Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.grid()
plt.show()


# In[14]:


sb.pairplot(ds)


# In[15]:


sb.pairplot(ds,hue='Category',diag_kind='hist')


# In[16]:


sb.pairplot(ds,hue='Region')


# In[17]:



ds['Category'].value_counts()
sb.countplot(x=ds['Category'])


# In[18]:


ds.corr()


# In[21]:


sb.heatmap(ds.corr(), annot=True)


# In[32]:


fig,axs=plt.subplots(nrows=2,ncols=2,figsize=(10,7));

sb.countplot(ds['Category'],ax=axs[0][0])
sb.countplot(ds['Segment'],ax=axs[0][1])
sb.countplot(ds['Ship Mode'],ax=axs[1][0])
sb.countplot(ds['Region'],ax=axs[1][1])
axs[0][0].set_title('Category',fontsize=20)
axs[0][1].set_title('Segment',fontsize=20)
axs[1][0].set_title('Ship Mode',fontsize=20)
axs[1][1].set_title('Region',fontsize=20)


# In[35]:


fig, axs = plt.subplots(ncols=2, nrows = 2, figsize = (10,10))
sb.distplot(ds['Sales'], color = 'red',  ax = axs[0][0])
sb.distplot(ds['Profit'], color = 'green',  ax = axs[0][1])
sb.distplot(ds['Quantity'], color = 'orange',  ax = axs[1][0])
sb.distplot(ds['Discount'], color = 'blue',  ax = axs[1][1])
axs[0][0].set_title('Sales Distribution', fontsize = 20)
axs[0][1].set_title('Profit Distribution', fontsize = 20)
axs[1][0].set_title('Quantity distribution', fontsize = 20)
axs[1][1].set_title('Discount Distribution', fontsize = 20)
plt.show()


# In[22]:


plt.title('Region')
plt.pie(ds['Region'].value_counts(),labels=ds['Region'].value_counts().index,autopct='%1.1f%%')
plt.show()


# In[23]:


plt.title('Ship Mode')
plt.pie(ds['Ship Mode'].value_counts(),labels=ds['Ship Mode'].value_counts().index,autopct='%1.1f%%')
plt.show()


# In[24]:


ds.groupby('Segment')['Profit'].sum().sort_values().plot.bar()
plt.title("Profits on various Segments")


# In[25]:


ds.groupby('Region')['Profit'].sum().sort_values().plot.bar()
plt.title("Profits on various Regions")


# In[26]:


plt.figure(figsize=(14,6))
ds.groupby('State')['Profit'].sum().sort_values().plot.bar()
plt.title("Profits on various States")

