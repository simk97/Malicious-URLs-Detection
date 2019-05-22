#!/usr/bin/env python
# coding: utf-8

# In[117]:


allTokens = []
def getTokens(input):
    tokensBySlash = str(input).split('/')
    allTokens = []
    for i in tokensBySlash:
        tokens = str(i).split('-')
        tokensByDot = []
        for j in range(0,len(tokens)):
            tempTokens = str(tokens[j]).split('.')
            tokensByDot = tokensByDot + tempTokens
        allTokens = allTokens + tokens + tokensByDot
        allTokens = list(set(allTokens))
        if 'com' in allTokens:
            allTokens.remove('com') 
return allTokens


# In[ ]:


import pandas as pd
import random
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
lgs = LogisticRegression()
vectorizer = TfidfVectorizer()
def TL():
    Data = 'http://web.archive.org/web/20181013193031/https://raw.githubusercontent.com/faizann24/Using-machine-learning-to-detect-malicious-URLs/master/data/data.csv'
    queriescsv = pd.read_csv(Data,',',error_bad_lines=False)
    queriesdf = pd.DataFrame(queriescsv)
    queriesdata = np.array(queriesdf)
    random.shuffle(queriesdata)
    y = [d[1] for d in queriesdata]
    corpus = [d[0] for d in queriesdata]
    vectorizer = TfidfVectorizer(tokenizer=getTokens(queriesdata))
    X = vectorizer.fit_transform(corpus) 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
    lgs = LogisticRegression() 
    lgs.fit(X_train, y_train)
    print(lgs.score(X_test, y_test))
    X_predict = ['wikipedia.com','google.com/search=faizanahad','pakistanifacebookforever.com/getpassword.php/','www.radsport-voggel.de/wp-admin/includes/log.exe','ahrenhei.without-transfer.ru/nethost.exe','www.itidea.it/centroesteticosothys/img/_notes/gum.exe'] #document.getElementById("input").value
    X_predict = vectorizer.transform(X_predict)
    y_Predict = lgs.predict(X_predict)
    print(y_Predict)
return vectorizer, lgs


# In[133]:


TL()

