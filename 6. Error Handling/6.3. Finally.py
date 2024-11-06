# 6.3 Finally - Menjamin Eksekusi Kode Terlepas Dari Terjadinya Error

# **Definisi Finally**:
# Blok `finally` dalam Python digunakan untuk mengeksekusi kode yang perlu dijalankan setelah blok `try-except`, 
# terlepas apakah terjadi kesalahan atau tidak. Ini sering digunakan untuk memastikan bahwa sumber daya yang dibuka (seperti file, 
# koneksi jaringan, atau database) akan selalu ditutup dengan benar, bahkan jika ada kesalahan yang terjadi di dalam blok `try`.

# **Sintaks dasar try-except-finally**:
# try:
#     # Blok kode yang mungkin menyebabkan error
# except <JenisError>:
#     # Blok kode untuk menangani error jika ada
# finally:
#     # Blok kode yang selalu dijalankan setelah try-except selesai

# **Contoh 1: Penggunaan finally untuk menutup file**
try:
    # Membuka file dan mencoba membaca isinya
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    # Jika file tidak ditemukan, menangani error
    print("File tidak ditemukan.")
finally:
    # Blok finally selalu dijalankan, untuk menutup file
    try:
        file.close()
        print("File berhasil ditutup.")
    except NameError:
        print("File belum dibuka, tidak dapat ditutup.")

# **Penjelasan**:
# - Pada contoh ini, kita mencoba membuka file dengan nama "example.txt" untuk dibaca.
# - Jika file tidak ditemukan, maka akan muncul pesan error melalui blok `except FileNotFoundError`.
# - Setelah itu, terlepas dari apakah terjadi kesalahan atau tidak, blok `finally` akan selalu mengeksekusi kode untuk menutup file.
#   Namun, jika file gagal dibuka (karena kesalahan atau file tidak ditemukan), blok `finally` akan tetap mencoba menutupnya,
#   dan menangani kemungkinan kesalahan (seperti `NameError` jika variabel `file` tidak didefinisikan).

# **Contoh 2: Penggunaan finally dalam koneksi database**
def koneksi_database():
    try:
        # Misalnya kita membuka koneksi ke database (contoh hanya untuk ilustrasi)
        print("Membuka koneksi database...")
        # Kode untuk membuka koneksi database
        koneksi = True
        print("Koneksi berhasil.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        # Blok finally selalu dijalankan, digunakan untuk menutup koneksi
        if koneksi:
            print("Menutup koneksi database...")
            # Kode untuk menutup koneksi database
            koneksi = False
        print("Koneksi ditutup.")

# Memanggil fungsi koneksi database
koneksi_database()

# **Penjelasan**:
# - Pada contoh ini, kita menggunakan blok `finally` untuk memastikan bahwa koneksi ke database akan selalu ditutup,
#   meskipun terjadi kesalahan dalam proses membuka koneksi.
# - Jika koneksi berhasil dibuka, maka kode di dalam `finally` akan menutup koneksi setelah operasi selesai, sehingga sumber daya
#   selalu dibebaskan dengan benar.

# **Contoh 3: Menggunakan finally dengan pengecualian yang terjadi**
try:
    # Mencoba untuk membagi dua angka
    x = 5
    y = 0
    hasil = x / y  # Akan menyebabkan ZeroDivisionError
except ZeroDivisionError:
    print("Tidak dapat membagi dengan nol!")
finally:
    print("Proses selesai, blok finally selalu dijalankan.")

# **Penjelasan**:
# - Program ini mencoba melakukan pembagian dengan nol, yang akan menyebabkan `ZeroDivisionError`.
# - Meskipun terjadi error, kode dalam blok `finally` akan tetap dijalankan, memastikan bahwa program tidak berhenti tanpa
#   menyelesaikan proses yang ada di blok `finally`.

# **Contoh 4: Blok finally yang tidak menangani error**
try:
    # Kode yang menyebabkan error
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
except ValueError:
    print("Input harus berupa angka.")
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol.")
finally:
    print("Program selesai, blok finally dieksekusi.")

# **Penjelasan**:
# - Pada contoh ini, kita mencoba melakukan pembagian dengan angka yang dimasukkan oleh pengguna.
# - Jika terjadi kesalahan, seperti memasukkan data yang bukan angka atau pembagian den
