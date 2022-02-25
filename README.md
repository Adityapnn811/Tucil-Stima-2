# Library Convex Hull

> Sebuah library python yang menyelesaikan masalah _convex hull_ menggunakan algoritma _Divide and Conquer_

## Daftar Isi
- [Deskripsi](#deskripsi)
- [Direktori](#direktori)
- [_Environment_](#environment)
- [Cara Menggunakan Library](#cara-menggunakan-library)
- [Cara _Run_ program](#cara-run-program)
- [Author](#author)

## Deskripsi
_Convex_ adalah himpunan titik pada bidang yang planar jika untuk sembarang dua titik pada bidang tersebut 
(misal p dan q), seluruh segmen garis yang berakhir di p dan q berada pada himpunan tersebut. _Convex hull_ dari sebuah
himpunan titik S adalah himpunan _convex_ terkecil (_convex polygon_) yang mengandung S. _Convex hull_ dapat
dimanfaatkan untuk _collision detection_ pada animasi komputer. Selain itu, _convex hull_ dapat mendeteksi _outliers_
pada kumpulan data. Penentuan _convex hull_ menggunakan algoritma _divide and conquer_ dengan cara mencari dua titik
yang membagi kumpulan titik menjadi dua, kemudian mencari titik yang membentuk sudut terbesar dengan dua titik pembagi. 
Setelah itu, dilakukan rekursif hingga tidak ada titik lain yang dapat membentuk sudut.

## Direktori
```
|──src
|   |──main.py
|   |──ConvexHull
|       |──__init__.py
|       |──convexHull.py
|       |──mathematics.py
|       |──sort.py
|──test
|   |──listData.txt         [Berisi list dataset yang digunakan untuk testing]
|──doc
|   |──Laporan.pdf          [Laporan Tugas Kecil 2 Stima]
|──README.md
```

## Environment dan Requirements
```
-Python 3.9
-Windows 10
-Library pandas python
-Library math python
-Library mathplotlib python
-

```

## Cara Menggunakan Library
1. Download folder `src` dari repository ini atau lakukan clone repository ini 
2. Lakukan import pada _script_ Anda dengan `import src.ConvexHull.[modul]`
3. Selesai!

## Cara Run Program
1. Download repository ini atau lakukan clone repository
2. Buka terminal pada folder repository ini, kemudian ganti direktori ke src dengan cara `cd src`
3. Jika Anda menggunakan windows, run `main.py` dengan perintah `py main.py`
4. Jika Anda menggunakan Linux based system, run `main.py` dengan perintah `python3 main.py`
5. Ikuti perintah pada terminal, program selesai dijalankan.

## Author
Aditya Prawira Nugroho - 13520049
