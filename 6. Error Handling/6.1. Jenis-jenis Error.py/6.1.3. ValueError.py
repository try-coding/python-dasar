# 6.1.3 ValueError - Kesalahan Nilai dalam Python

# **Definisi ValueError**:
# - `ValueError` terjadi ketika operasi atau fungsi dijalankan dengan nilai yang tidak sesuai, meskipun tipe data yang digunakan benar.
# - Kesalahan ini terjadi ketika fungsi menerima argumen dengan tipe data yang benar, tetapi nilainya tidak sesuai dengan yang diharapkan.

# **Contoh 1: Mengkonversi string yang tidak dapat dikonversi ke angka**
angka_str = "abc"
angka = int(angka_str)  # Kesalahan: Tidak dapat mengkonversi "abc" ke dalam integer

# **Penjelasan:**
# Fungsi `int()` mengharapkan argumen yang bisa dikonversi menjadi integer, seperti string "123". 
# Namun, jika argumen yang diberikan bukan representasi angka yang valid, seperti string "abc", maka Python akan menghasilkan `ValueError`.
#
# Contoh yang menyebabkan ValueError:
# ValueError: invalid literal for int() with base 10: 'abc'

# **Contoh 2: Menggunakan metode yang tidak cocok dengan tipe data**
angka = "123"
angka = angka.replace(1, 2)  # Kesalahan: Metode replace() mengharapkan string sebagai argumen pertama dan kedua

# **Penjelasan:**
# Pada contoh di atas, kita mencoba mengganti karakter '1' dengan karakter '2' pada string "123" menggunakan `replace()`.
# Namun, metode `replace()` mengharapkan dua argumen yang keduanya adalah string, bukan angka. 
# Ini menyebabkan `ValueError` karena argumen yang diberikan tidak sesuai.
#
# Contoh yang menyebabkan ValueError:
# ValueError: replace() argument 1 must be str, not int

# **Contoh 3: Menggunakan fungsi dengan nilai yang tidak valid untuk tipe data tertentu**
def bagi(a, b):
    if b == 0:
        raise ValueError("Pembagian dengan nol tidak diperbolehkan.")
    return a / b

# Memanggil fungsi dengan nilai yang tidak sesuai
try:
    print(bagi(10, 0))  # Kesalahan: Pembagian dengan nol
except ValueError as e:
    print(e)  # Output: Pembagian dengan nol tidak diperbolehkan.

# **Penjelasan:**
# Fungsi `bagi()` memeriksa jika nilai kedua adalah nol sebelum melakukan pembagian. 
# Jika nilai kedua adalah nol, fungsi akan menampilkan `ValueError` dengan pesan yang sesuai.
#
# Contoh yang menyebabkan ValueError:
# ValueError: Pembagian dengan nol tidak diperbolehkan.

# **Contoh 4: Menyediakan argumen yang salah untuk fungsi atau metode**
angka = "42.5"
hasil = int(angka)  # Kesalahan: Tidak dapat mengkonversi angka desimal (float) ke integer tanpa pembulatan

# **Penjelasan:**
# Kita mencoba mengkonversi string "42.5" menjadi integer menggunakan `int()`. Namun, string ini adalah representasi angka desimal, 
# yang tidak dapat langsung dikonversi menjadi integer tanpa pembulatan. Fungsi `int()` tidak menerima angka desimal dalam bentuk string, 
# sehingga menghasilkan `ValueError`.
#
# Contoh yang menyebabkan ValueError:
# ValueError: invalid literal for int() with base 10: '42.5'

# **Kesimpulan**:
# - `ValueError` terjadi ketika fungsi atau operasi menerima nilai yang benar tipe datanya, tetapi nilainya tidak sesuai atau tidak valid untuk operasi tersebut.
# - Penyebab umum `ValueError` meliputi:
#   1. Mengkonversi nilai yang tidak valid ke dalam tipe data lain (misalnya, mencoba mengkonversi string "abc" menjadi integer).
#   2. Menyediakan nilai yang tidak sesuai untuk fungsi atau metode yang mengharapkan nilai tertentu.
#   3. Membuat operasi yang tidak valid secara logika, seperti pembagian dengan nol.
# - Untuk menghindari `ValueError`, pastikan bahwa nilai yang diberikan sesuai dengan yang diharapkan oleh fungsi atau operasi yang Anda lakukan.

