import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import myConvexHull.convexHull as ch
import random

# inisiasi array warna
colors = ['darkviolet','cyan','yellow','lightcoral','b','r','g', 'deeppink', 'purple']
colorPicked = []

# Input dataset
print("List dataset yang tersedia: ")
print("1. iris ")
print("2. wine ")
print("3. breast cancer ")
inputData = int(input("Masukan nomor dataset yang Anda inginkan: "))
while not 1<= inputData <= 3:
    print("Input diluar batas")
    inputData = int(input("Masukan nomor dataset yang Anda inginkan: "))
# Load dataset berdasarkan masukan pengguna
if inputData == 1:
    data = datasets.load_iris()
    print("Kolom yang ingin divisualisasikan: ")
    print("1. Sepal Width vs Sepal Length")
    print("2. Petal Width vs Petal Length")
    inputTitle = int(input("Masukan nomor pilihan: "))
    while not 1<= inputTitle <= 2:
        print("Input diluar batas")
        inputTitle = int(input("Masukan nomor pilihan: "))
    if inputTitle == 1:
        awal = 0
        akhir = 1
        title = "Sepal Width vs Sepal Length"
    else:
        awal = 2
        akhir = 3
        title = "Petal Width vs Petal Length"
elif inputData == 2:
    data = datasets.load_wine()
    print("Kolom yang ingin divisualisasikan: ")
    print("1. Alcohol vs Malic Acid")
    print("2. Ash vs Alcalinity of Ash")
    inputTitle = int(input("Masukan nomor pilihan: "))
    while not 1<= inputTitle <= 2:
        print("Input diluar batas")
        inputTitle = int(input("Masukan nomor pilihan: "))
    if inputTitle == 1:
        awal = 0
        akhir = 1
        title = "Alcohol vs Malic Acid"
    else:
        awal = 2
        akhir = 3
        title = "Ash vs Alcalinity of Ash"
else:
    data = datasets.load_breast_cancer()
    print("Kolom yang ingin divisualisasikan: ")
    print("1. Mean Radius vs Mean Texture")
    print("2. Mean Perimeter vs Mean Area")
    inputTitle = int(input("Masukan nomor pilihan: "))
    while not 1<= inputTitle <= 2:
        print("Input diluar batas")
        inputTitle = int(input("Masukan nomor pilihan: "))
    if inputTitle == 1:
        awal = 0
        akhir = 1
        title = "Mean Radius vs Mean Texture"
    else:
        awal = 2
        akhir = 3
        title = "Mean Perimeter vs Mean Area"

# Buat DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
pd.set_option("max_column", None)

#visualisasi hasil ConvexHull
plt.figure(figsize = (10, 6))
plt.title(title)
plt.xlabel(data.feature_names[awal])
plt.ylabel(data.feature_names[akhir])
for i in range(len(data.target_names)):
    colorNum = random.randint(0, 6)
    # Mencegah warna sama
    while colorNum in colorPicked:
        colorNum = random.randint(0, 6)
    colorPicked.append(colorNum)
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[awal,akhir]].values
    hull = ch.myConvexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i], color=colors[colorNum])
    for simplex in hull:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[colorNum])
plt.legend()
print("Apakah Anda ingin menyimpan diagram?")
save = input("Input Y/N: ")
if (save == "Y" or save == 'y'):
    namaFile = input("Masukan nama file: ")
    plt.savefig("../src/" + namaFile + ".png")
    print("Gambar berhasil disimpan di folder src dengan nama file " + namaFile + ".png")
plt.show()
