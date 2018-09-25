import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.cluster import KMeans
import jieba
from sklearn import metrics
from collections import namedtuple

data = pd.read_csv('new_csv_to_csv.csv', usecols=[0])

print(data.shape)
#print(data)

result1 = []
result2 = []
def getData(data):
    for index, row in data.iterrows():
        data = list(row[0].split('\t'))
        for a in data:
            result = jieba.cut(a)
            result = ' '.join(result)
            result1.append(result)
            result2.append(a)

        #print(data)
    print(result1[1])
    return result1, result2




newData,oldData  = getData(data)
print(newData[2], oldData[2])
#
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(newData)

tfidf  = TfidfTransformer()
X = tfidf.fit_transform(X.toarray())
#print(newData)
print(X)

kmeans = KMeans(n_clusters=100, max_iter=300, n_init=1, init='k-means++', n_jobs=1)
#kmeans.fit(X.toarray())

pred = kmeans.fit_predict(X.toarray())

# with open('result.csv','a',encoding='utf-8') as f:
#      f.write()
for i in range(len(pred)):
    print(oldData[i], pred[i])

    with open('result1.csv', 'a', encoding='utf-8') as f:
        f.write(oldData[i]+','+str(pred[i])+"\n")




