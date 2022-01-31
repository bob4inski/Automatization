#import re
import pandas as pd
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from pymorphy2 import MorphAnalyzer
import numpy as np
import matplotlib.pyplot as plt

loaded_data = pd.read_csv('Задание.csv', sep='\t', )

bad_words = "[A-Za-z0-9!#$%&'()*+,./:;<=>?@[\]^_{|}~\"\-]+"
morph = MorphAnalyzer()
def token_only(text):
    text = re.sub(bad_words,' ',text)
    tokens = [word.lower() for sent in sent_tokenize(text) for word in word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        token = token.strip()
        token = morph.normal_forms(token)[0]
        filtered_tokens.append(token)
    return filtered_tokens


dfclall = loaded_data['']
stopwords = stopwords.words('russian')
stopwords.extend(['итог','руб','который','клиент'])
tfidf_vectorizer = TfidfVectorizer(smooth_idf=True,max_df=0.6,min_df=0.01,max_features=100000,
                                   stop_words=stopwords,
                                   use_idf=True,tokenizer=token_only, ngram_range=(1,3))
tfidf_matrix = tfidf_vectorizer.fit_transform(dfclall)

mbk  = MiniBatchKMeans(n_clusters=200,init='random').fit(tfidf_matrix)
y_kmeansMBK = mbk.predict(tfidf_matrix)
Num = []
Num = [pt for pt in y_kmeansMBK]
df2 = {"Num_Cluster": Num}
dfMBK = pd.DataFrame(df2)
df = pd.concat([dfClaster,dfMBK], axis=1)
df.to_excel('Claster.xlsx', index=False)