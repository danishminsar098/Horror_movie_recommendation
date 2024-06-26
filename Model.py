#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[6]:


df = pd.read_csv('horror_movies.csv')


# In[7]:


df.head()


# In[8]:


df.info()


# In[9]:


mov= df[['id','original_title','overview','genre_names']]
mov


# In[10]:


mov.isnull().sum()


# In[11]:


mov = mov.dropna()
mov.shape


# In[12]:


mov = mov.applymap(lambda x: x.replace('Horror','') if isinstance(x, str) else x)


# In[13]:


mov['tags'] = mov['genre_names'] +mov['overview']


# 

# In[14]:


mov= mov[['id','original_title','tags']]
mov


# In[15]:


mov=mov[mov['tags' ].str.contains( 'Add a Plot' )==False ]
\


mov.shape


# In[27]:


mov= mov.dropna().reset_index(drop=True)


# In[37]:


mov.shape


# In[29]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')
    


# In[31]:


vector = cv.fit_transform(mov['tags']).toarray()


# In[ ]:





# In[32]:


from sklearn.metrics.pairwise import cosine_similarity


# In[33]:


similarity = cosine_similarity(vector)


# In[ ]:


sorted(list(enumerate(similarity[0])),reverse=True,key = lambda x: x[1])   #how much similar


# In[35]:


mov.memory_usage()


# In[39]:


def recommend(movie):
    index = mov[mov['original_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:11]:
        print(mov.iloc[i[0]].original_title)


# In[47]:


recommend('Rows')


# In[41]:


import pickle
pickle.dump(mov,open('movie_list.pkl','wb'))


# In[48]:


pickle.dump(similarity,open('similarity.pkl','wb'))

