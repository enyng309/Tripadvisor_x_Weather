import csv
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import math
from fractions import Fraction

data = pd.read_csv('./hotel_review1.csv')
data = data.drop(data.columns[[0]], axis = 'columns') # index 열 삭제
feature = data[["score", "review_number"]]

model = KMeans(n_clusters=3)
model.fit(feature)

predict = pd.DataFrame(model.predict(feature))
predict.columns = ['predict']

r = pd.concat([data, predict], axis = 1)
r = r.sort_values(["predict"], ascending=True)  # predict 순서로 정렬
r = r.reset_index(drop=True) # 인덱스도 다시 정렬
r.to_csv('hotel_kmeans_sort.csv')
print(r)

# scatter plot
plt.scatter(r['score'], r['review_number'], c = r['predict'], alpha=0.5)
plt.show()

index_0 = r[r['predict'] == 0].index
r = r.drop(index_0)
print(r)
r = r.reset_index(drop=True) # 인덱스도 다시 정렬
r.to_csv('hotel_recommend.csv')