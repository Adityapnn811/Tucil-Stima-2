"""TODO: - Refaktor karena pake fungsi determinan (done) tapi pemakaiannya masi salah, ini nyambung ke pembagian listTitik
        - cek fungsi yang ngebagi listTitik ke dua bagian
        - POKOKNYA CEK NGEBAGI LISTTITIK SAMA PASSING TITIK TITIK KE REKURSIF TERUTAMA TITIK UJUNG UJUNG
        - Cek yang mencari jarak antara titik dengan garis (done)
        - yang jarak itu, kelompokkin nilai A, b sama c dulu dari rumus (done)
"""
import math
# Fungsi untuk menghitung determinan dari 3 titik
def determinan(x1, y1, x2, y2, x3, y3):
    # (x1, y1) membentuk garis dengan (x2, y2), (x3, y3) adalah titik yang dicari
    return ((x1 * y2) + (x3 * y1) + (x2 * y3)) - ((x3 * y2) + (x2 * y1) + (x1 * y3))


# Fungsi menghasilkan jarak antar titik
def jarakDuaTitik(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# Fungsi mencari tinggi segitiga (jarak titik dengan garis) setelah diketahui luas dan alas
def sudutTigaTitik(x1, y1, x2, y2, x3, y3):
    u = [(x1 - x2), (y1 - y2)]
    v = [(x1 - x3), (y1 - y3)]
    udotv = u[0] * v[0] + u[1] * v[1]
    panjangU = (u[0]**2 + u[1]**2)**0.5
    panjangV = (v[0]**2 + v[1]**2)**0.5
    # print(udotv, panjangU, panjangV)
    return math.acos(udotv/(panjangU * panjangV))
    # # Menggunakan rumus mencari garis, kemudian gunakan d = Ax + By + C / sqrt(A^2 + B^2)
    # A = 1/(x2 - x1)
    # B = -1/(y2 - y1)
    # C = (y1/(y2 - y1)) - (x1/(x2 - x1))
    # return abs((A * x3 + B * y3 + C) / (A ** 2 + B ** 2) ** 0.5)

# Fungsi untuk melakukan sorting list titik terurut dari terkecil ke besar
# Akan melakukan sorting berdasarkan Y jika byY = 1, X jika 0
def sortList(listTitik, byY):
    temp = [[0, 0]]
    swapping = True
    byX = 1
    if byY == 1:
        byX = 0
    maxStep = len(listTitik)
    i = 0
    while i < maxStep and swapping:
        swapping = False
        for j in range(0, maxStep - i - 1):
            if listTitik[j][byY] > listTitik[j + 1][byY]:

                temp[0][byY] = listTitik[j][byY]
                temp[0][byX] = listTitik[j][byX]

                listTitik[j][byY] = listTitik[j + 1][byY]
                listTitik[j][byX] = listTitik[j + 1][byX]

                listTitik[j + 1][byY] = temp[0][byY]
                listTitik[j + 1][byX] = temp[0][byX]
                swapping = True
    return listTitik


# Fungsi yang melakukan merge dua titik
def merge(listIndeks1, listIndeks2):
    listIndeksHasil = []
    if listIndeks1 != None:
        for i in range (0, len(listIndeks1)):
            if listIndeks1[i] not in listIndeksHasil:
                listIndeksHasil.append(listIndeks1[i])
    if listIndeks2 != None:

        for i in range (0, len(listIndeks2)):
            if listIndeks2[i] not in listIndeksHasil:
                listIndeksHasil.append(listIndeks2[i])
    return listIndeksHasil


# Fungsi yang mencari jarak maksimum, listTitik tidak kosong. Mengembalikan indeks titik maksimum
def sudutMaks(i1, i_n, listTitik, listIndeks):
    max = 0
    idx = 0
    for i in listIndeks:
        if (sudutTigaTitik(listTitik[i1][0], listTitik[i1][1], listTitik[i_n][0], listTitik[i_n][1], listTitik[i][0], listTitik[i][1])) > max:
            max = sudutTigaTitik(listTitik[i1][0], listTitik[i1][1], listTitik[i_n][0], listTitik[i_n][1], listTitik[i][0], listTitik[i][1])
            idx = i
    return idx


# Fungsi mencari S1 dan S2
def findS1AndS2(listTitik, listIndeks, i1, i_n):
    S1 = []
    S2 = []

    for i in listIndeks:
        if i != i1 and i != i_n:
            if determinan(listTitik[i1][0], listTitik[i1][1], listTitik[i_n][0], listTitik[i_n][1], listTitik[i][0], listTitik[i][1]) > 0:
                S1.append(i)
            elif determinan(listTitik[i1][0], listTitik[i1][1], listTitik[i_n][0], listTitik[i_n][1], listTitik[i][0], listTitik[i][1]) < 0:
                S2.append(i)
    return S1, S2


# Fungsi yang mencari titik terluar bagian atas secara rekursif
def searchHullUp(listTitik, listIndeksUp, i1, i2):
    # basis saat list Titik tinggal 1
    if len(listIndeksUp) < 1:
        hasil = [[i1, i2]]
        return hasil
    else:
        # Cari indeks maksimum
        idx_pmax = sudutMaks(i1, i2, listTitik, listIndeksUp)
        # Cari S1 dan S2 lagi untuk i1 pmax dan i2 pmax
        S11, unused = findS1AndS2(listTitik, listIndeksUp, i1, idx_pmax)
        S12, unused2 = findS1AndS2(listTitik, listIndeksUp, idx_pmax, i2)
        # S2 tidak terpakai karena dia di dalam bangun

        return merge(searchHullUp(listTitik, S11, i1, idx_pmax), searchHullUp(listTitik, S12, idx_pmax, i2))


# Fungsi yang mencari titik terluar bagian bawah secara rekursif
def searchHullDown(listTitik, listIndeksDown, i1, i2):
    # basis saat list Titik tinggal 1
    if len(listIndeksDown) < 1:
        return [[i1, i2]]
    else:
        # Cari indeks maksimum
        idx_pmax = sudutMaks(i1, i2, listTitik, listIndeksDown)
        # Cari S1 dan S2 lagi untuk i1 pmax dan i2 pmax
        unused, S11 = findS1AndS2(listTitik, listIndeksDown, i1, idx_pmax)
        unused2, S12 = findS1AndS2(listTitik, listIndeksDown, idx_pmax, i2)
        # S2 tidak terpakai karena dia di dalam bangun

        return merge(searchHullDown(listTitik, S11, i1, idx_pmax), searchHullDown(listTitik, S12, idx_pmax, i2))


# Fungsi myConvexHull
def myConvexHull(listTitik):
    # Basis adalah ketika listTitik tinggal 1
    if listTitik.shape[0] <= 3:
        return [0, 1, 2]
    else:
        # selain itu, cari dua titik yang membagi menjadi dua (atas bawah)
        # listTitik = sortList(listTitik, 0)
        listIndeks = []
        for i in range(len(listTitik)):
            listIndeks.append(i)
        # Indeks awal dan indeks akhir
        iAwal = listIndeks[0]
        iAkhir = listIndeks[-1]
        # Buat S1 dan S2, S1 adalah titik yang di atas
        listIndeks.remove(listIndeks[0])
        listIndeks.remove(listIndeks[-1])
        S1, S2 = findS1AndS2(listTitik, listIndeks, iAwal, iAkhir)
        hull = merge(searchHullUp(listTitik, S1, iAwal, iAkhir), searchHullDown(listTitik, S2, iAwal, iAkhir))
        return hull

