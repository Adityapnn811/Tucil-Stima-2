"""TODO: - Laporan, readme, struktur kde
        - Comment dan modular kode (done)

"""
import ConvexHull.sort as s
import ConvexHull.mathematics as m

# Fungsi yang melakukan merge dua list indeks
def merge(listIndeks1, listIndeks2):
    listIndeksHasil = []
    # Cek apakah lisIndeks1 atau 2 kosong
    if listIndeks1 != None:
        for i in range (0, len(listIndeks1)):
            # Cek jika listIndeks1[i] tidak ada duplikat
            if listIndeks1[i] not in listIndeksHasil:
                listIndeksHasil.append(listIndeks1[i])
    if listIndeks2 != None:
        for i in range (0, len(listIndeks2)):
            if listIndeks2[i] not in listIndeksHasil:
                listIndeksHasil.append(listIndeks2[i])
    return listIndeksHasil


# Fungsi mencari S1 dan S2 dan mengembalikan S1 dan S2 yang berupa list dari indeks titik
def findS1AndS2(listTitik, listIndeks, i1, i_n):
    S1 = []
    S2 = []

    for i in listIndeks:
        # Cek apakah indeks dari listIndeks sama dengan indeks maks dan min
        if i != i1 and i != i_n:
            if m.determinan(listTitik[i1][0], listTitik[i1][1], listTitik[i_n][0], listTitik[i_n][1], listTitik[i][0],
                          listTitik[i][1]) > 0:
                S1.append(i)
            elif m.determinan(listTitik[i1][0], listTitik[i1][1], listTitik[i_n][0], listTitik[i_n][1], listTitik[i][0],
                            listTitik[i][1]) < 0:
                S2.append(i)
    return S1, S2


# Fungsi yang mencari indeks titik terluar bagian atas secara rekursif
def searchHullUp(listTitik, listIndeksUp, i1, i2):
    # basis saat listIndeksUp kosong
    if len(listIndeksUp) < 1:
        hasil = [[i1, i2]]
        return hasil
    else:
        # Cari indeks titik maksimum
        idx_pmax = m.sudutMaks(i1, i2, listTitik, listIndeksUp)
        # Cari S1 dan S2 lagi untuk i1 idx_pmax dan i2 idx_pmax
        S11, unused = findS1AndS2(listTitik, listIndeksUp, i1, idx_pmax)
        S12, unused2 = findS1AndS2(listTitik, listIndeksUp, idx_pmax, i2)
        # bagian bawah tidak terpakai karena dia di dalam bangun

        return merge(searchHullUp(listTitik, S11, i1, idx_pmax), searchHullUp(listTitik, S12, idx_pmax, i2))


# Fungsi yang mencari indeks titik terluar bagian bawah secara rekursif
def searchHullDown(listTitik, listIndeksDown, i1, i2):
    # basis saat listIndeksDown kosong
    if len(listIndeksDown) < 1:
        return [[i1, i2]]
    else:
        # Cari indeks titik maksimum
        idx_pmax = m.sudutMaks(i1, i2, listTitik, listIndeksDown)
        # Cari S1 dan S2 lagi untuk i1 idx_pmax dan i2 idx_pmax
        unused, S11 = findS1AndS2(listTitik, listIndeksDown, i1, idx_pmax)
        unused2, S12 = findS1AndS2(listTitik, listIndeksDown, idx_pmax, i2)
        # bagian atas tidak terpakai karena dia di dalam bangun

        return merge(searchHullDown(listTitik, S11, i1, idx_pmax), searchHullDown(listTitik, S12, idx_pmax, i2))


# Fungsi ConvexHull, mengembalikan list Indeks yang sudah berpasangan dan siap untuk di-plot
def myConvexHull(listTitik):
    # Sorting titik dahulu
    listTitik = s.sortList(listTitik, 0)
    # Buat sebuah list indeks titik urut dari 0 hingga panjang listTitik
    listIndeks = []
    for i in range(len(listTitik)):
        listIndeks.append(i)
    # Simpan indeks awal dan indeks akhir
    iAwal = listIndeks[0]
    iAkhir = listIndeks[-1]
    # Delete indeks 0 dan indeks terakhir agar tidak terjadi pengulangan
    listIndeks.remove(listIndeks[0])
    listIndeks.remove(listIndeks[-1])
    # Cari S1 dan S2
    S1, S2 = findS1AndS2(listTitik, listIndeks, iAwal, iAkhir)
    # Lakukan rekursif
    hull = merge(searchHullUp(listTitik, S1, iAwal, iAkhir), searchHullDown(listTitik, S2, iAwal, iAkhir))
    return hull
