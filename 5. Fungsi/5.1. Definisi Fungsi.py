# 5.1 Definisi Fungsi - Cara Mendefinisikan dan Menggunakan Fungsi dalam Python

# Fungsi dalam Python adalah sebuah blok kode yang dapat digunakan kembali untuk menjalankan suatu tugas tertentu.
# Fungsi memungkinkan kita untuk menghindari pengulangan kode yang sama dan membuat program lebih terstruktur dan modular.

# **Struktur dasar mendefinisikan fungsi**:
# def nama_fungsi(parameter1, parameter2, ...):
#     # Blok kode yang akan dijalankan saat fungsi dipanggil
#     # Kode dalam fungsi biasanya menghasilkan nilai atau efek samping (seperti mencetak hasil)

# Fungsi dalam Python didefinisikan dengan kata kunci 'def', diikuti dengan nama fungsi dan tanda kurung.
# Di dalam tanda kurung bisa berisi parameter (opsional), dan setelah tanda kurung diikuti dengan blok kode yang akan dijalankan.

# Contoh 1: Fungsi sederhana tanpa parameter dan tanpa return
def sapa():
    print("Halo, selamat datang di Python!")

# Untuk memanggil fungsi, kita cukup menulis nama fungsi diikuti tanda kurung.
sapa()  # Output: Halo, selamat datang di Python!

# **Penjelasan:**
# - Fungsi 'sapa' tidak membutuhkan parameter dan hanya mencetak pesan ke layar saat dipanggil.
# - Fungsi didefinisikan dengan kata kunci 'def', diikuti dengan nama fungsi dan tanda kurung.

# Fungsi bisa mengerjakan banyak tugas, seperti menghitung nilai, memanipulasi data, atau mencetak output ke layar.
# Fungsi membuat kode lebih modular dan memudahkan pemeliharaan program.

# Contoh 2: Fungsi dengan parameter
def sapa_nama(nama):
    print(f"Halo, {nama}! Selamat datang di Python.")

# Memanggil fungsi dengan memberikan argumen
sapa_nama("Andi")  # Output: Halo, Andi! Selamat datang di Python.

# **Penjelasan:**
# - Fungsi 'sapa_nama' memiliki satu parameter 'nama' yang digunakan dalam pesan sapaan.
# - Parameter memungkinkan kita untuk mengirimkan nilai saat memanggil fungsi. Nilai ini akan digunakan dalam fungsi.

# **Kesimpulan:**
# Fungsi memungkinkan kita untuk menyusun program dengan lebih efisien dan menghindari pengulangan kode.
# Fungsi juga memberikan cara untuk memisahkan tugas-tugas tertentu dalam kode sehingga lebih mudah dipahami dan dipelihara.

