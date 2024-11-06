# 4.2.1 For Loop - Perulangan untuk Menyusuri Iterasi

# For loop adalah salah satu cara untuk melakukan perulangan dalam Python.
# Biasanya, for loop digunakan untuk menyusuri elemen-elemen dalam suatu iterable, seperti list, string, atau range.

# **Struktur dasar for loop**:
# for variabel in iterable:
#     # Blok kode yang akan dijalankan untuk setiap elemen dalam iterable

# Berikut adalah contoh sederhana menggunakan for loop untuk menyusuri list.

# Contoh 1: Menyusuri elemen dalam list
buah = ["apel", "pisang", "ceri", "durian"]

for item in buah:
    # Setiap elemen dalam list 'buah' akan disimpan sementara dalam variabel 'item'
    print(item)  # Menampilkan setiap elemen dalam list

# Output:
# apel
# pisang
# ceri
# durian
# Pada contoh ini, setiap elemen dalam list 'buah' akan dicetak satu per satu.

# **Penjelasan:**
# - Di sini, 'buah' adalah iterable (list) yang berisi beberapa elemen.
# - Pada setiap iterasi, variabel 'item' akan berisi nilai elemen dari list tersebut.
# - Perintah 'print(item)' akan menampilkan nilai elemen satu per satu.

# Contoh 2: Menggunakan for loop dengan range()
# Fungsi range() menghasilkan urutan angka yang bisa digunakan untuk perulangan.
# Range dapat menerima dua parameter: mulai dan selesai (exclusive).

for i in range(5):
    # Range menghasilkan angka dari 0 hingga 4 (5 tidak termasuk)
    print(i)  # Menampilkan angka dari 0 hingga 4

# Output:
# 0
# 1
# 2
# 3
# 4
# Fungsi range(5) menghasilkan angka 0 sampai 4. 

# **Penjelasan:**
# - Fungsi range() menghasilkan urutan angka. Dalam contoh ini, range(5) berarti menghasilkan angka dari 0 sampai 4.
# - Variabel 'i' akan mengambil nilai dari angka yang dihasilkan oleh range, dan perintah 'print(i)' akan menampilkan nilai tersebut.

# Contoh 3: Menyusuri elemen dalam string
# String juga merupakan iterable, yang berarti kita bisa menggunakan for loop untuk menyusuri karakter-karakter dalam string.

kata = "Python"

for karakter in kata:
    # Setiap karakter dalam string 'kata' akan disimpan dalam variabel 'karakter'
    print(karakter)

# Output:
# P
# y
# t
# h
# o
# n
# Dalam contoh ini, setiap karakter dalam string 'kata' akan ditampilkan satu per satu.

# **Penjelasan:**
# - String 'Python' adalah iterable, sehingga kita bisa menyusuri setiap karakter dalam string tersebut menggunakan for loop.
# - Pada setiap iterasi, variabel 'karakter' berisi karakter yang sedang diproses, dan print(karakter) menampilkan karakter tersebut.

# Contoh 4: Perulangan dengan indeks menggunakan enumerate()
# Fungsi enumerate() memungkinkan kita untuk mendapatkan indeks dan nilai dalam iterable.

buah = ["apel", "pisang", "ceri", "durian"]

for indeks, item in enumerate(buah):
    # enumerate(buah) menghasilkan pasangan indeks dan nilai
    print(f"Indeks {indeks}: {item}")

# Output:
# Indeks 0: apel
# Indeks 1: pisang
# Indeks 2: ceri
# Indeks 3: durian
# Dengan enumerate, kita bisa mendapatkan indeks dan nilai pada saat yang bersamaan.

# **Penjelasan:**
# - Fungsi enumerate() mengembalikan pasangan (indeks, nilai) untuk setiap elemen dalam iterable.
# - Dalam contoh ini, kita dapat memperoleh indeks dan item pada saat yang sama, yang berguna jika kita perlu mengetahui posisi elemen.

# Contoh 5: Perulangan dengan range() dengan dua parameter (start, stop)
# Kita juga bisa menggunakan range dengan dua parameter untuk menentukan batas awal dan akhir iterasi.

for i in range(2, 8):
    # Range akan menghasilkan angka mulai dari 2 sampai 7 (8 tidak termasuk)
    print(i)

# Output:
# 2
# 3
# 4
# 5
# 6
# 7

# **Penjelasan:**
# - Range(2, 8) berarti kita akan mulai dari angka 2 dan berhenti di angka 7, karena angka 8 tidak disertakan.
# - Ini memungkinkan kita untuk menentukan batasan yang lebih fleksibel untuk perulangan.

# Contoh 6: For loop dengan langkah (step) menggunakan range()
# Range juga dapat menerima parameter ketiga, yaitu langkah (step), untuk menentukan selisih antar angka yang dihasilkan.

for i in range(0, 10, 2):
    # Range akan menghasilkan angka mulai dari 0 hingga 8, dengan langkah 2
    print(i)

# Output:
# 0
# 2
# 4
# 6
# 8
# Di sini, langkahnya adalah 2, sehingga program hanya menghasilkan angka genap dari 0 sampai 8.

# **Penjelasan:**
# - Dalam range(0, 10, 2), angka dimulai dari 0, dan setiap iterasi menambahkan 2 ke angka sebelumnya.
# - Ini berguna untuk membuat perulangan dengan interval tertentu.

# **Kesimpulan:**
# - **For loop** sangat berguna untuk melakukan perulangan pada elemen-elemen dalam iterable, seperti list, string, tuple, atau angka yang dihasilkan oleh range().
# - Dengan menggunakan **range()**, kita dapat membuat perulangan dengan berbagai rentang dan langkah yang fleksibel.
# - Fungsi **enumerate()** memungkinkan kita untuk mendapatkan indeks dan nilai pada saat yang bersamaan dalam perulangan.
