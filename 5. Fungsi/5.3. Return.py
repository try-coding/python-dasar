# 5.3 Return - Mengembalikan Nilai dari Fungsi

# **Definisi return**:
# - Kata kunci `return` digunakan dalam sebuah fungsi untuk mengembalikan nilai ke pemanggil fungsi.
# - Fungsi yang memiliki `return` akan mengembalikan suatu nilai yang dapat digunakan lebih lanjut dalam program.
# - Setelah `return` dipanggil, eksekusi fungsi akan berhenti dan nilai yang dikembalikan akan diteruskan ke pemanggil fungsi.

# **Contoh 1: Fungsi dengan return untuk mengembalikan nilai**
def jumlahkan(a, b):
    hasil = a + b
    return hasil  # Mengembalikan hasil penjumlahan a dan b

# Memanggil fungsi dan menyimpan hasilnya dalam variabel
total = jumlahkan(5, 3)
print("Hasil penjumlahan:", total)  # Output: Hasil penjumlahan: 8

# **Penjelasan:**
# - Fungsi 'jumlahkan' menerima dua parameter, yaitu 'a' dan 'b', yang dijumlahkan di dalam fungsi.
# - Nilai hasil penjumlahan dikembalikan dengan `return`, dan hasil tersebut disimpan dalam variabel 'total'.
# - Nilai yang dikembalikan oleh `return` digunakan di luar fungsi (di luar cakupan fungsi).

# **Contoh 2: Fungsi dengan return yang mengembalikan lebih dari satu nilai (Multiple Return)**
def hitung_luas_keliling(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling  # Mengembalikan dua nilai sekaligus sebagai tuple

# Memanggil fungsi dan menampung hasilnya dalam dua variabel
luas, keliling = hitung_luas_keliling(10, 5)
print("Luas:", luas)           # Output: Luas: 50
print("Keliling:", keliling)   # Output: Keliling: 30

# **Penjelasan:**
# - Fungsi 'hitung_luas_keliling' mengembalikan dua nilai sekaligus, yaitu 'luas' dan 'keliling', yang dikemas dalam bentuk tuple.
# - Kita dapat menangkap kedua nilai tersebut dengan cara menuliskan dua variabel untuk menerima hasil return dari fungsi.

# **Contoh 3: Fungsi dengan return tanpa nilai**
def tidak_ada_hasil():
    print("Fungsi ini tidak mengembalikan apa-apa.")
    return  # return tanpa nilai

# Memanggil fungsi tanpa mengharapkan nilai kembali
tidak_ada_hasil()  # Output: Fungsi ini tidak mengembalikan apa-apa.

# **Penjelasan:**
# - Fungsi 'tidak_ada_hasil' menggunakan `return` tanpa memberikan nilai apa pun.
# - Fungsi tetap bisa mengembalikan sesuatu (meskipun tidak ada nilai yang diberikan), dan eksekusi fungsi berhenti setelah `return` dipanggil.
# - Jika tidak ada `return` sama sekali, fungsi akan mengembalikan `None` secara otomatis.

# **Contoh 4: Menggunakan return untuk menghentikan eksekusi fungsi lebih awal**
def bagi(a, b):
    if b == 0:
        return "Error: Pembagi tidak boleh 0"  # Menghentikan fungsi jika pembagi adalah 0
    return a / b

# Memanggil fungsi dengan argumen yang valid
hasil = bagi(10, 2)
print("Hasil bagi:", hasil)  # Output: Hasil bagi: 5.0

# Memanggil fungsi dengan argumen yang tidak valid (bagi 0)
error = bagi(10, 0)
print(error)  # Output: Error: Pembagi tidak boleh 0

# **Penjelasan:**
# - Fungsi 'bagi' mengembalikan error message jika pembagi bernilai 0.
# - `return` digunakan di awal fungsi untuk menghentikan eksekusi lebih lanjut jika kondisi tertentu terpenuhi.

# **Kesimpulan:**
# - `return` digunakan untuk mengembalikan nilai dari fungsi ke pemanggilnya.
# - Fungsi dapat mengembalikan satu nilai atau beberapa nilai (dalam bentuk tuple).
# - Jika tidak ada `return`, fungsi akan mengembalikan `None` secara default.
# - `return` juga dapat digunakan untuk menghentikan eksekusi fungsi lebih awal, seperti pada pengecekan kondisi tertentu (misalnya pembagi 0 dalam contoh).

