import pandas as pd
from sklearn.cluster import KMeans
import joblib
import pymorphy2
import pymystem3

loaded_data = pd.read_csv('Задание.csv', sep='\t')
print(loaded_data.head(3))

X = loaded_data

kmeans = KMeans(n_clusters=2, random_state=0) # создаём объект модели, настриваем параметры
kmeans = kmeans.fit(X) # обучаем модель





# save
joblib.dump(clf, "model.pkl") 

# load
clf2 = joblib.load("model.pkl")

clf2.predict(X[0:1])