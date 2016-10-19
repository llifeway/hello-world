
# coding: utf-8

# In[19]:

import requests
from bs4 import BeautifulSoup
res = requests.get("https://tw.buy.yahoo.com/?sub=583")
#print res.text
soup = BeautifulSoup(res.text)
print soup.select('div')[10]



# In[ ]:



