# 6.2 Try-Except - Menangani Kesalahan dengan Try-Except

# **Definisi Try-Except**:
# Struktur `try-except` digunakan untuk menangani kesalahan (error) yang terjadi selama eksekusi program.
# Dengan menggunakan `try-except`, kita dapat menangkap dan menangani error yang muncul, 
# sehingga program dapat tetap berjalan tanpa berhenti secara tiba-tiba.

# **Sintaks dasar try-except**:
# try:
#     # Kode yang mungkin menyebabkan error
# except <JenisError>:
#     # Kode yang akan dijalankan jika terjadi error

# **Contoh 1: Menangani kesalahan dengan try-except**
try:
    # Mengambil input dari pengguna dan mencoba mengkonversinya ke integer
    user_input = input("Masukkan angka: ")
    number = int(user_input)
    print(f"Angka yang Anda masukkan adalah {number}")
except ValueError:
    # Jika terjadi ValueError (misalnya input bukan angka), tampilkan pesan error
    print("Terjadi kesalahan! Input bukan angka yang valid.")

# **Penjelasan**:
# - Pada kode ini, program mencoba untuk mengkonversi input yang diberikan oleh pengguna menjadi angka menggunakan `int()`.
# - Jika input yang diberikan bukan angka yang valid, Python akan menghasilkan `ValueError` dan mengeksekusi blok `except`, 
#   menampilkan pesan kesalahan bahwa input bukan angka yang valid.

# **Contoh 2: Menangani beberapa jenis error**
try:
    # Mengambil dua input dari pengguna dan mencoba melakukan pembagian
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    hasil = angka1 / angka2
    print(f"Hasil pembagian: {hasil}")
except ValueError:
    # Jika input bukan angka yang valid
    print("Kesalahan! Harap masukkan angka yang valid.")
except ZeroDivisionError:
    # Jika pembagi adalah nol
    print("Kesalahan! Tidak dapat membagi dengan nol.")
except Exception as e:
    # Menangani kesalahan lainnya
    print(f"Terjadi kesalahan tak terduga: {e}")

# **Penjelasan**:
# - Program ini meminta dua input angka dari pengguna dan mencoba membagi angka pertama dengan angka kedua.
# - Ada beberapa pengecualian yang ditangani:
#   1. **ValueError**: Jika input bukan angka yang valid.
#   2. **ZeroDivisionError**: Jika pembagian dilakukan dengan angka nol.
#   3. **Exception**: Menangkap kesalahan lainnya yang tidak tercakup oleh pengecualian spesifik sebelumnya.
#   - Penggunaan `Exception` di akhir berfungsi untuk menangkap semua jenis kesalahan lainnya yang tidak secara eksplisit dihadapi.

# **Contoh 3: Menangani kesalahan tanpa menentukan jenis error**
try:
    # Kode yang menyebabkan error
    x = 10 / 0  # Pembagian dengan nol
except:
    # Menangkap kesalahan apa pun yang terjadi tanpa spesifikasi jenis error
    print("Terjadi kesalahan saat melakukan pembagian.")

# **Penjelasan**:
# - Pada contoh ini, tidak ada jenis error yang ditentukan setelah `except`.
# - Ini akan menangkap **semua jenis kesalahan** yang terjadi di dalam blok `try`, tanpa membedakan jenis error.
# - Namun, pendekatan ini tidak dianjurkan karena bisa menangkap kesalahan yang tidak relevan atau tidak diinginkan.

# **Contoh 4: Menangani kesalahan dengan else dan finally**
try:
    # Mengambil input angka dan melakukan pembagian
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    hasil = angka1 / angka2
except ZeroDivisionError:
    # Menangani kesalahan pembagian dengan nol
    print("Tidak dapat membagi dengan nol.")
else:
    # Blok else hanya dijalankan jika tidak ada error yang terjadi
    print(f"Hasil pembagian adalah: {hasil}")
finally:
    # Blok finally selalu dijalankan, baik terjadi error maupun tidak
    print("Terimakasih telah menggunakan kalkulator.")

# **Penjelasan**:
# - Blok `else` hanya dijalankan jika tidak ada pengecualian yang terjadi di blok `try`.
# - Blok `finally` selalu dijalankan setelah blok `try-except` selesai, tidak peduli apakah terjadi kesalahan atau tidak.
# - `finally` sering digunakan untuk membersihkan sumber daya atau melakukan tugas yang perlu dijalankan terlepas dari adanya kesalahan.

# **Kesimpulan**:
# - `try-except` adalah cara utama untuk menangani error dalam Python, yang membantu untuk menjaga program tetap berjalan meskipun terjadi kesalahan.
# - Anda dapat menangani berbagai jenis pengecualian menggunakan beberapa `except` atau menangani semua pengecualian menggunakan `except` tanpa jenis error.
# - Blok `else` dijalankan jika tidak ada pengecualian, sementara blok `finally` selalu dijalankan setelah blok `try-except`, terlepas dari apakah terjadi error atau tidak.
# - Dengan menggunakan `try-except`, Anda dapat mengelola kesalahan dengan lebih elegan dan memberikan pengalaman pengguna yang lebih baik, seperti memberikan pesan kesalahan yang jelas dan mencegah program berhenti mendadak.

