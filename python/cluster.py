import os
os.chdir("../Dataset/Second dataset")
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
#%matplotlib inline
df = pd.read_excel("022_preprocessing_after_normalizing_values.xlsx")
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.savefig('elbow.png')
plt.show()
_____________________________________________________

kmeans = KMeans(n_clusters = 3, n_init = 20, n_jobs = 1) # n_init(number of iterations for clsutering) n_jobs(number of cpu cores to use)
kmeans.fit(df)
# We look at 3 the clusters generated by k-means.
#common_words = kmeans.cluster_centers_.argsort()[:,-1:-26:-1]
#for num, centroid in enumerate(common_words):
 #   print(str(num) + ' : ' + ', '.join(words[word] for word in centroid))