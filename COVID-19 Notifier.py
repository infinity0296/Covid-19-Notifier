#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Desktop Notifier for COVID-19
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier


# In[11]:


header = {"user-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
html = urlopen(req)


# In[8]:


html.status


# In[12]:


obj = bs(html)


# In[16]:


new_cases = obj.find("li",{"class":"news_li"}).strong.text.split()[0]


# In[17]:


death = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]


# In[20]:


#Notifier


# In[21]:


notifier = ToastNotifier()


# In[22]:


message  = "New Cases - "+ new_cases+"\nDeath - "+death


# In[23]:


message


# In[25]:


notifier.show_toast(title="COVID-19 Update", msg=message, duration=5, icon_path=r"virus.ico")


# In[ ]:




