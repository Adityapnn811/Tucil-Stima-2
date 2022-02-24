import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from myConvexHull import sortList, myConvexHull

data = datasets.load_iris()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
pd.set_option("max_column", None)

#visualisasi hasil ConvexHull
from scipy.spatial import ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    # Lakukan sorting terhadap bucket
    bucket = sortList(bucket, 0)
    hull = myConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    # # Buat sebuah matriks titik hull berdekatan
    # hullTuple = []
    # for point in hull:
    #     hullTuple.append([point, jarakMin(point, hull)])
    # print("ini hultuple")
    # print(hullTuple)
    # Buat sebuah tuple yang berisi list koordinat x dan y, kemudian plot
    # for l in range(len(hullTuple)):
    #     listX = [hullTuple[l][0][0], hullTuple[l][1][0]]
    #     listY = [hullTuple[l][0][1], hullTuple[l][1][1]]
    #     plt.plot(listX, listY, colors[i])
    # print(i)
    # print(bucket[hull.vertices])
    for simplex in hull:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()
plt.show()
