import math


# Fungsi untuk menghitung determinan dari 3 titik
def determinan(x1, y1, x2, y2, x3, y3):
    # (x1, y1) membentuk garis dengan (x2, y2). (x3, y3) adalah titik maksimum baru
    return ((x1 * y2) + (x3 * y1) + (x2 * y3)) - ((x3 * y2) + (x2 * y1) + (x1 * y3))


# Fungsi menghasilkan jarak antar titik
def jarakDuaTitik(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# Fungsi mencari sudut dari tiga titik, yaitu sudut (x2, y2)
def sudutTigaTitik(x1, y1, x2, y2, x3, y3):
    # Menggunakan rumus vektor
    u = [(x1 - x2), (y1 - y2)]
    v = [(x1 - x3), (y1 - y3)]
    udotv = u[0] * v[0] + u[1] * v[1]
    panjangU = (u[0] ** 2 + u[1] ** 2) ** 0.5
    panjangV = (v[0] ** 2 + v[1] ** 2) ** 0.5
    return math.acos(udotv / (panjangU * panjangV))


# Fungsi yang mencari jarak maksimum, listTitik tidak kosong. Mengembalikan indeks titik maksimum
def sudutMaks(i1, i_n, listTitik, listIndeks):
    maks = 0
    idx = 0
    for i in listIndeks:
        if (sudutTigaTitik(listTitik[i1][0], listTitik[i1][1], listTitik[i_n][0], listTitik[i_n][1], listTitik[i][0],
                           listTitik[i][1])) > maks:
            maks = sudutTigaTitik(listTitik[i1][0], listTitik[i1][1], listTitik[i_n][0], listTitik[i_n][1],
                                  listTitik[i][0], listTitik[i][1])
            idx = i
    return idx
