# 7.1 Penamaan Variabel - Aturan dan Praktik Terbaik

# **Definisi**:
# Variabel adalah tempat penyimpanan data yang dapat digunakan untuk menyimpan nilai atau referensi ke objek.
# Penamaan variabel yang benar sangat penting untuk membuat kode Python menjadi lebih mudah dibaca dan dipahami.

# **Aturan Penamaan Variabel dalam Python**:
# 1. Variabel harus dimulai dengan huruf (a-z, A-Z) atau garis bawah (_).
# 2. Setelah karakter pertama, variabel dapat terdiri dari huruf, angka (0-9), atau garis bawah (_).
# 3. Nama variabel tidak boleh mengandung spasi.
# 4. Nama variabel bersifat case-sensitive, artinya 'variabel' dan 'Variabel' adalah dua nama yang berbeda.
# 5. Nama variabel tidak boleh sama dengan kata kunci (reserved words) dalam Python (seperti if, while, for, etc.).
# 6. Variabel sebaiknya memiliki nama yang deskriptif, menggambarkan nilai atau fungsi variabel tersebut.

# **Contoh Penamaan Variabel yang Benar**:
nama_depan = "Andi"   # Benar: dimulai dengan huruf
umur = 25             # Benar: hanya menggunakan huruf dan angka
total_harga = 100000  # Benar: menggunakan underscore sebagai pemisah kata
namaUser = "Budi"     # Benar: menggunakan camelCase

# **Contoh Penamaan Variabel yang Salah**:
# 1. Menggunakan angka di awal nama variabel
# 2. Menggunakan spasi dalam nama variabel
# 3. Menggunakan kata kunci (reserved words) sebagai nama variabel

# 1. Salah: Variabel tidak boleh diawali dengan angka
# 3_angka = 100  # Salah: Variabel ini masih benar, karena diawali dengan angka setelah underscore, jadi ini sah.
# 2. Salah: Nama variabel tidak boleh mengandung spasi
# nama depan = "John"  # Salah: Menggunakan spasi yang tidak diizinkan dalam nama variabel.
# 3. Salah: Kata kunci tidak boleh digunakan sebagai nama variabel
# if = "Ini adalah kata kunci!"  # Salah: 'if' adalah kata kunci Python dan tidak bisa digunakan sebagai nama variabel

# **Kata Kunci Python** (Reserved Words):
# Python memiliki daftar kata kunci yang sudah digunakan untuk tujuan tertentu, 
# dan kita tidak dapat menggunakan kata kunci ini sebagai nama variabel.

import keyword
print("Daftar kata kunci Python:", keyword.kwlist)

# **Praktik Terbaik dalam Penamaan Variabel**:
# 1. Gunakan nama variabel yang deskriptif untuk memudahkan pemahaman kode.
#    Misalnya, 'nama_depan' lebih jelas daripada hanya 'x' atau 'a'.
nama_barang = "Laptop"  # Deskriptif, menggambarkan barang yang dimaksud.
harga_barang = 15000000  # Deskriptif, menggambarkan harga barang.

# 2. Gunakan huruf kecil dan underscore (_) untuk pemisah kata (snake_case).
total_harga_produk = 10000  # Snake case yang lebih mudah dibaca.

# 3. Hindari penggunaan nama variabel yang terlalu singkat kecuali dalam konteks tertentu
#    seperti loop index (i, j, k, dsb).
for i in range(10):  # i, j, k biasanya digunakan dalam loop.
    print(i)

# 4. Gunakan camelCase untuk penamaan variabel dalam gaya penulisan tertentu
#    (meskipun snake_case lebih umum di Python).
# Misalnya, dalam pengembangan web (Javascript, atau dalam beberapa standar proyek), camelCase lebih sering digunakan.
userAge = 30  # Camel case, biasa digunakan dalam JavaScript atau di beberapa framework.

# **Kesimpulan**:
# - Penamaan variabel harus mengikuti aturan yang jelas untuk memastikan kode mudah dibaca dan bebas dari error.
# - Gunakan nama yang deskriptif dan hindari nama variabel yang ambigu atau menggunakan kata kunci Python.
# - Praktik terbaik adalah menggunakan gaya penulisan yang konsisten seperti snake_case untuk Python.
# - Memahami dan mengikuti aturan penamaan variabel akan meningkatkan kualitas kode dan memudahkan debugging.

