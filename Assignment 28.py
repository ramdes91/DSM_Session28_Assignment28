
# coding: utf-8

# Problem Statement
# 
# In this assignment students have to find the frequency of words in a webpage. User can
# use urllib and BeautifulSoup to extract text from webpage.

# In[5]:


from bs4 import BeautifulSoup 
import urllib.request 
import nltk 
nltk.download('stopwords')
from nltk.corpus import stopwords 
response = urllib.request.urlopen('http://php.net/') 
html = response.read() 
soup = BeautifulSoup(html,"html5lib") 
text = soup.get_text(strip=True) 
tokens = [t for t in text.split()] 
clean_tokens = tokens[:] 
sr = stopwords.words('english') 
for token in tokens: 
    if token in stopwords.words('english'): 
        clean_tokens.remove(token) 
freq = nltk.FreqDist(clean_tokens) 
for key,val in freq.items(): 
    print (str(key) + ':' + str(val))


# In[3]:


freq.plot(20,cumulative=False)

