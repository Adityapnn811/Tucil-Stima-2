# Fungsi untuk melakukan sorting list titik terurut dari terkecil ke besar
# Akan melakukan sorting berdasarkan Y jika byY = 1, X jika byY = 0
def sortList(listTitik, byY):
    temp = [[0, 0]]
    swapping = True
    # jika byY = 0, maka byX = 1, begitu pula sebaliknya
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
