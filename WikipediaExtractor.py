#!/usr/bin/env python
# coding: utf-8

# In[68]:


import requests
import csv

from bs4 import BeautifulSoup

r=requests.get("https://en.wikipedia.org/wiki/Sachin_Tendulkar")

c=r.content



soup=BeautifulSoup(c,"html.parser")

all=soup.find("table",{"class":"infobox vcard"})



output_rows = []
for i in all.findAll('tr'):
    header = i.findAll('th')
    columns = i.findAll('td')
    output_row = []
    for j in header:
        output_row.append(j.text)
        for k in columns:
            output_row.append(k.text)
    output_rows.append(output_row)

with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


# In[ ]:





# In[ ]:




