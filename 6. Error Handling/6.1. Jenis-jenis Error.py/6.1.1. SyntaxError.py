# 6.1.1 SyntaxError - Kesalahan Sintaksis dalam Python

# **Definisi SyntaxError**:
# - `SyntaxError` adalah jenis error yang terjadi ketika Python tidak dapat mengerti kode karena kesalahan dalam aturan sintaksis bahasa Python.
# - Kesalahan ini muncul ketika kode tidak mengikuti struktur atau format yang benar sesuai dengan aturan Python.

# **Contoh 1: Kurangnya tanda titik dua (:) setelah definisi fungsi**
def sapa():
    print("Halo, selamat datang!")

# **Penjelasan:**
# Fungsi ini benar dan tidak ada error. Namun, jika kita menghapus tanda titik dua (:) setelah 'def sapa' seperti berikut:
# def sapa()
# Maka Python akan memberikan SyntaxError karena tanda titik dua (:) di akhir deklarasi fungsi wajib ada.
#
# Contoh yang menyebabkan SyntaxError:
# def sapa()  # Kesalahan: Harus ada tanda titik dua (:) setelah definisi fungsi.
# SyntaxError: expected ':' after function definition

# **Contoh 2: Kurang tanda kurung dalam struktur if statement**
if 5 > 3
    print("5 lebih besar dari 3")
    
# **Penjelasan:**
# Kesalahan ini terjadi karena kita lupa menambahkan tanda titik dua (:) setelah kondisi pada statement if.
# Dalam Python, setiap blok kode kontrol (seperti if, else, while, for, dll.) harus diakhiri dengan tanda titik dua (:) di akhir kondisinya.
#
# Contoh yang menyebabkan SyntaxError:
# if 5 > 3  # Kesalahan: Harus ada titik dua setelah kondisi if.
# SyntaxError: invalid syntax

# **Contoh 3: Kesalahan dalam tanda kutip pada string**
message = "Halo, selamat datang!
print(message)

# **Penjelasan:**
# Kesalahan terjadi karena tanda kutip pembuka dan penutup tidak konsisten.
# Python mengharuskan string dimulai dan diakhiri dengan tanda kutip yang sama (' atau ").
# Jika kita tidak menutup string dengan benar, maka akan terjadi SyntaxError.
#
# Contoh yang menyebabkan SyntaxError:
# message = "Halo, selamat datang!  # Kesalahan: Tanda kutip penutup hilang.
# SyntaxError: EOL while scanning string literal

# **Contoh 4: Ketidaksesuaian indentasi**
def hitung():
  x = 5
    y = 10  # Kesalahan: indentasi salah pada baris kedua.
    print(x + y)

# **Penjelasan:**
# Python sangat memperhatikan indentasi untuk menentukan blok kode. 
# Jika indentasi tidak konsisten (misalnya, menggunakan spasi di satu baris dan tab di baris lain), Python akan memberikan SyntaxError.
#
# Contoh yang menyebabkan SyntaxError:
# def hitung():
#   x = 5
#     y = 10  # Kesalahan: Baris kedua tidak memiliki indentasi yang benar.
# SyntaxError: expected an indented block

# **Kesimpulan:**
# - `SyntaxError` terjadi saat Python tidak bisa memahami kode karena aturan sintaksis yang dilanggar.
# - Penyebab umum `SyntaxError` meliputi:
#   1. Tidak ada tanda titik dua setelah deklarasi fungsi atau struktur kontrol.
#   2. Kurangnya tanda kutip penutup pada string.
#   3. Kesalahan indentasi dalam blok kode.
# - Untuk menghindari `SyntaxError`, pastikan untuk mematuhi aturan sintaksis Python dengan benar, seperti penggunaan tanda titik dua, tanda kutip yang sesuai, dan indentasi yang konsisten.

