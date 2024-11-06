# 6.1.2 TypeError - Kesalahan Tipe Data dalam Python

# **Definisi TypeError**:
# - `TypeError` terjadi ketika operasi atau fungsi dijalankan dengan tipe data yang tidak sesuai.
# - Kesalahan ini muncul ketika Anda mencoba melakukan operasi yang tidak mendukung tipe data tertentu, misalnya menambahkan angka ke string atau mencoba menggabungkan tipe data yang tidak kompatibel.

# **Contoh 1: Menambahkan angka dan string**
angka = 5
teks = "Python"
hasil = angka + teks  # Kesalahan: Tidak dapat menambahkan integer dan string bersama-sama

# **Penjelasan:**
# Pada contoh di atas, kita mencoba menambahkan integer (5) ke string ("Python").
# Operasi penambahan (+) antara tipe data integer dan string tidak diperbolehkan, sehingga Python akan menghasilkan TypeError.
#
# Contoh yang menyebabkan TypeError:
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# **Contoh 2: Memanggil metode pada tipe data yang salah**
angka = 10
hasil = angka.upper()  # Kesalahan: Fungsi upper() hanya berlaku untuk tipe data string

# **Penjelasan:**
# Fungsi `upper()` digunakan untuk mengubah semua huruf dalam string menjadi huruf besar.
# Namun, pada contoh ini, kita mencoba memanggil metode `upper()` pada sebuah integer (angka), yang bukan tipe data yang mendukung metode tersebut.
# Ini akan menyebabkan TypeError karena `upper()` hanya bisa digunakan pada objek bertipe `str`.
#
# Contoh yang menyebabkan TypeError:
# TypeError: 'int' object has no attribute 'upper'

# **Contoh 3: Menggunakan fungsi dengan argumen yang salah tipe**
def bagi(a, b):
    return a / b

# Memanggil fungsi dengan argumen yang tidak sesuai
print(bagi(10, "5"))  # Kesalahan: Tidak dapat membagi integer dengan string

# **Penjelasan:**
# Pada contoh di atas, fungsi `bagi()` mengharapkan kedua argumen untuk menjadi angka (misalnya integer atau float).
# Tetapi, kita mencoba membagi angka dengan string ("5"). Hal ini menyebabkan TypeError karena operasi pembagian tidak bisa dilakukan antara tipe data `int` dan `str`.
#
# Contoh yang menyebabkan TypeError:
# TypeError: unsupported operand type(s) for /: 'int' and 'str'

# **Contoh 4: Menggabungkan list dengan tipe data yang tidak sesuai**
list1 = [1, 2, 3]
list2 = "abc"
hasil = list1 + list2  # Kesalahan: Tidak dapat menggabungkan list dengan string

# **Penjelasan:**
# Pada contoh ini, kita mencoba menggabungkan dua objek dengan tipe data yang berbeda: sebuah list dengan sebuah string.
# Di Python, operasi penambahan (concatenation) hanya dapat dilakukan pada objek yang kompatibel, seperti dua list atau dua string, tetapi bukan antara list dan string.
#
# Contoh yang menyebabkan TypeError:
# TypeError: can only concatenate list (not "str") to list

# **Contoh 5: Mencoba untuk mengakses metode atau atribut yang tidak ada pada tipe data tertentu**
angka = 5
hasil = angka.append(10)  # Kesalahan: tipe data 'int' tidak memiliki metode 'append'

# **Penjelasan:**
# Metode `append()` hanya dapat digunakan untuk objek tipe data list, bukan tipe data integer.
# Dalam contoh ini, kita mencoba memanggil metode `append()` pada sebuah integer, yang tidak memiliki metode tersebut.
#
# Contoh yang menyebabkan TypeError:
# TypeError: 'int' object has no attribute 'append'

# **Kesimpulan:**
# - `TypeError` terjadi ketika operasi atau fungsi dijalankan dengan tipe data yang tidak sesuai.
# - Penyebab umum `TypeError` meliputi:
#   1. Menggunakan operator matematika atau string dengan tipe data yang tidak kompatibel (misalnya mencoba menambahkan integer dengan string).
#   2. Memanggil metode yang tidak ada pada tipe data tertentu (misalnya mencoba menggunakan metode string pada integer).
#   3. Menggunakan argumen yang tidak sesuai tipe pada suatu fungsi.
# - Untuk menghindari `TypeError`, pastikan bahwa operasi yang Anda lakukan sesuai dengan tipe data yang benar dan kompatibel.

