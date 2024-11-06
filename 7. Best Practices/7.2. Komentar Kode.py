# 7.2 Komentar Kode - Menggunakan Komentar untuk Menjelaskan Kode

# **Definisi Komentar**:
# Komentar adalah bagian dari kode yang tidak dieksekusi oleh Python. Komentar digunakan untuk memberi penjelasan atau catatan dalam kode, 
# yang bertujuan untuk memudahkan pemahaman kode oleh programmer lain atau oleh diri kita sendiri di kemudian hari.

# Komentar sangat berguna untuk menjelaskan tujuan dari kode tertentu, mengapa suatu cara digunakan, atau untuk memberi peringatan mengenai 
# kemungkinan bug atau kekurangan dalam kode.

# **Jenis Komentar dalam Python**:
# 1. **Komentar Satu Baris**: Menggunakan tanda pagar (#)
# 2. **Komentar Multibaris (Block Comments)**: Menggunakan tanda kutip tiga (""" atau ''')
# 3. **Docstrings (Komentar Dokumentasi)**: Digunakan untuk mendokumentasikan fungsi, kelas, atau modul menggunakan tanda kutip tiga.

# **1. Komentar Satu Baris**:
# Komentar satu baris diawali dengan tanda pagar (#). 
# Segala sesuatu setelah tanda pagar (#) pada baris tersebut akan dianggap sebagai komentar dan tidak akan dieksekusi.

# Contoh komentar satu baris:
x = 10  # Menyimpan angka 10 dalam variabel x
y = 5   # Menyimpan angka 5 dalam variabel y
result = x + y  # Menjumlahkan x dan y

# **2. Komentar Multibaris (Block Comments)**:
# Jika kita perlu memberikan penjelasan yang lebih panjang atau menjelaskan lebih dari satu baris, kita bisa menggunakan komentar block.
# Komentar block dimulai dengan tanda pagar (#) di setiap barisnya.

# Contoh komentar multibaris:
# Menghitung hasil penjumlahan antara dua angka
# Variabel x dan y masing-masing menyimpan angka 10 dan 5
# Kemudian hasil penjumlahan disimpan dalam variabel result
# Program ini menampilkan hasil penjumlahan tersebut.

x = 10
y = 5
result = x + y

# **3. Docstrings (Komentar Dokumentasi)**:
# Docstrings adalah komentar khusus yang digunakan untuk mendokumentasikan fungsi, kelas, atau modul.
# Docstrings diletakkan di dalam tanda kutip tiga (""" atau ''') dan dapat meliputi beberapa baris.
# Docstrings digunakan untuk menjelaskan tujuan dan cara penggunaan suatu fungsi, kelas, atau modul.

# Contoh docstring untuk fungsi:
def tambah(a, b):
    """
    Fungsi ini menerima dua argumen a dan b, lalu mengembalikan hasil penjumlahannya.
    
    Parameters:
    a (int): Angka pertama yang akan dijumlahkan.
    b (int): Angka kedua yang akan dijumlahkan.
    
    Returns:
    int: Hasil penjumlahan antara a dan b.
    """
    return a + b

# Memanggil fungsi dan melihat dokumentasinya
print(tambah(3, 4))  # Output: 7

# **Penjelasan**:
# - Docstring dimulai dan diakhiri dengan tanda kutip tiga, dan biasanya berada tepat setelah definisi fungsi, kelas, atau modul.
# - Docstring berfungsi untuk menjelaskan apa yang dilakukan oleh fungsi atau kelas, argumen yang diterima, dan nilai yang dikembalikan (return).
# - Dokumen ini dapat dilihat dengan menggunakan bantuan fungsi `help()`, misalnya: `help(tambah)`.

# **Menggunakan Komentar untuk Debugging**:
# Komentar juga berguna dalam proses debugging. Misalnya, kita dapat menonaktifkan sementara kode yang menyebabkan masalah 
# dengan mengomentarinya dan menjalankan sisa kode.

# Contoh penggunaan komentar untuk debugging:
# x = 10
# y = 0  # Baris ini akan menyebabkan pembagian dengan nol, sehingga di-comment untuk debugging
# result = x / y
# print(result)  # Kode ini tidak akan dijalankan jika baris di atas dikomentari

# **Praktik Terbaik dalam Menggunakan Komentar**:
# 1. **Komentar untuk penjelasan kode yang kompleks**: Gunakan komentar untuk menjelaskan bagian kode yang sulit dipahami atau rumit.
#    Jangan berlebihan dalam memberi komentar di bagian kode yang sudah jelas.
#    Misalnya, komentar sederhana seperti "# Menambahkan dua angka" untuk operasi yang mudah dipahami tidak perlu dilakukan.

# 2. **Hindari komentar yang tidak perlu**: Jangan menambahkan komentar untuk hal-hal yang jelas dari nama variabel atau logika kode.
#    Sebagai contoh, kode berikut tidak memerlukan komentar tambahan:
x = 5  # Ini tidak diperlukan, karena sudah jelas apa yang dilakukan oleh kode ini.
y = 10  # Tidak perlu komentar juga.

# 3. **Gunakan komentar untuk menjelaskan *"mengapa"* sesuatu dilakukan, bukan hanya *"apa"* yang dilakukan**.
#    Menjelaskan alasan di balik pemilihan suatu pendekatan atau algoritma akan sangat membantu orang lain yang membaca kode kita.

# 4. **Komentar jangan terlalu panjang atau bertele-tele**: Komentar harus singkat, jelas, dan langsung pada inti masalah.

# **Kesimpulan**:
# - Komentar dalam kode Python sangat berguna untuk menjelaskan dan mendokumentasikan kode.
# - Gunakan komentar satu baris (#) untuk penjelasan yang singkat dan jelas.
# - Gunakan komentar multibaris untuk penjelasan yang lebih panjang atau untuk menjelaskan bagian yang lebih besar.
# - Gunakan docstrings untuk mendokumentasikan fungsi, kelas, dan modul.
# - Hindari komentar berlebihan atau tidak perlu, terutama jika kode sudah cukup jelas.
