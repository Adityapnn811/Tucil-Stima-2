"""TODO: - Refaktor karena pake fungsi determinan (done) tapi pemakaiannya masi salah, ini nyambung ke pembagian listTitik
        - cek fungsi yang ngebagi listTitik ke dua bagian
        - POKOKNYA CEK NGEBAGI LISTTITIK SAMA PASSING TITIK TITIK KE REKURSIF TERUTAMA TITIK UJUNG UJUNG
        - Cek yang mencari jarak antara titik dengan garis (done)
        - yang jarak itu, kelompokkin nilai A, b sama c dulu dari rumus (done)
"""
# Fungsi untuk menghitung determinan dari 3 titik
def determinan(x1, y1, x2, y2, x3, y3):
    # (x1, y1) membentuk garis dengan (x2, y2), (x3, y3) adalah titik yang dicari
    return (x1 * y2 + x3 * y1 + x2 * y3) - (x3 * y2 + x2 * y1 + x1 * y3)


# Fungsi menghasilkan jarak antar titik
def jarakDuaTitik(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# Fungsi mencari luas segitiga yang terbentuk oleh garis dengan titik
def luasSegitiga(x1, y1, x2, y2, x3, y3):
    # (x1, y1) dan (x2, y2) adalah garis asli
    garis = round(jarakDuaTitik(x1, y1, x2, y2), 6)
    garis_b = round(jarakDuaTitik(x1, y1, x3, y3), 6)
    garis_c = round(jarakDuaTitik(x2, y2, x3, y3), 6)
    semiperimeter = round(0.5 * (garis + garis_b + garis_c), 6)
    return (semiperimeter * (semiperimeter - garis) * (semiperimeter - garis_b) * (semiperimeter - garis_c)) ** 0.5


# Fungsi mencari tinggi segitiga (jarak titik dengan garis) setelah diketahui luas dan alas
def jarakTitikGaris(x1, y1, x2, y2, x3, y3):
    # Menggunakan rumus mencari garis, kemudian gunakan d = Ax + By + C / sqrt(A^2 + B^2)
    A = 1/(x2 - x1)
    B = -1/(y2 - y1)
    C = (y1/(y2 - y1)) - (x1/(x2 - x1))
    return abs((A * x3 + B * y3 + C) / (A ** 2 + B ** 2) ** 0.5)

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
def merge(listTitik1, listTitik2):
    listTitikHasil = []
    if listTitik1 != None:
        for i in range (0, len(listTitik1)):
            listTitikHasil.append(listTitik1[i])
    if listTitik2 != None:
        for i in range (0, len(listTitik2)):
            listTitikHasil.append(listTitik2[i])
    return listTitikHasil


# Fungsi yang mencari jarak maksimum, listTitik tidak kosong. Mengembalikan indeks titik maksimum
def jarakMaks(p1, pn, listTitik):
    max = jarakTitikGaris(p1[0], p1[1], pn[0], pn[1], listTitik[0][0], listTitik[0][1])
    idx = 0
    for i in range(1, len(listTitik)):
        if (jarakTitikGaris(p1[0], p1[1], pn[0], pn[1], listTitik[i][0], listTitik[i][1])) > max:
            max = jarakTitikGaris(p1[0], p1[1], pn[0], pn[1], listTitik[i][0], listTitik[i][1])
            idx = i
    return idx


# Fungsi yang mencari titik terluar secara rekursif
def searchHull(listTitik, p1, p2, pmax):
    # basis saat list Titik tinggal 1
    if len(listTitik) <= 1:
        return listTitik
    else:
        # Cari S1 dan S2 lagi
        S1 = []
        S2 = []
        for i in range(0, len(listTitik)):
            if determinan(p1[0], p1[1], pmax[0], pmax[1], listTitik[i][0], listTitik[i][1]) > 0:
                S1.append(listTitik[i])
            if determinan(p2[0], p2[1], pmax[0], pmax[1], listTitik[i][0], listTitik[i][1]) < 0:
                S2.append(listTitik[i])
        if len(S1) > 0 and len(S2) > 0:
            idx_pmax1 = jarakMaks(p1, pmax, S1)
            idx_pmax2 = jarakMaks(p2, pmax, S2)
            return merge(searchHull(S1, p1, pmax, S1[idx_pmax1]), searchHull(S2, p2, pmax, S2[idx_pmax2]))
        elif len(S1) > 0 and len(S2) == 0:
            idx_pmax1 = jarakMaks(p1, pmax, S1)
            # print(idx_pmax1, S1, p1, pmax)
            return searchHull(S1, p1, pmax, S1[idx_pmax1])
        elif len(S1) == 0 and len(S2) > 0:
            idx_pmax2 = jarakMaks(p2, pmax, S2)
            return searchHull(S2, p1, pmax, S2[idx_pmax2])



# Fungsi myConvexHull
def myConvexHull(listTitik):
    # Basis adalah ketika listTitik tinggal 1
    if listTitik.shape[0] <= 3:
        return listTitik
    else:
        # selain itu, cari dua titik yang membagi menjadi dua (atas bawah)
        # print(listTitik)
        listTitik = sortList(listTitik, 0)
        print(listTitik)
        p1 = listTitik[0] # p1 adalah titik paling bawah
        pn = listTitik[-1] # pn adalah titik paling atas
        # Buat S1 dan S2, S1 adalah titik yang di atas
        S1 = []
        S2 = []

        for i in range(1, listTitik.shape[0] - 1):
            if determinan(p1[0], p1[1], pn[0], pn[1], listTitik[i][0], listTitik[i][1]) > 0:
                S1.append(listTitik[i])
            elif determinan(p1[0], p1[1], pn[0], pn[1], listTitik[i][0], listTitik[i][1]) < 0:
                S2.append(listTitik[i])
        # print(S1, p1)
        # cari pmax1 dan pmax2
        idx_pmax1 = jarakMaks(p1, pn, S1)
        idx_pmax2 = jarakMaks(p1, pn, S2)
        hull = merge(searchHull(S1, p1, pn, S1[idx_pmax1]), searchHull(S2, p1, pn, S2[idx_pmax2]))
        hull.append(p1)
        hull.append(pn)
        print(hull)

