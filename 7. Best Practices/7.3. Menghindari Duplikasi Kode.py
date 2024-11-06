# 7.3 Menghindari Duplikasi Kode - Praktik Terbaik untuk Menulis Kode yang Bersih

# **Definisi Duplikasi Kode**:
# Duplikasi kode terjadi ketika bagian kode yang sama muncul di beberapa tempat dalam program.
# Hal ini dapat menyebabkan kesulitan dalam pemeliharaan kode, karena jika terjadi perubahan pada satu bagian kode, 
# kita harus memperbarui semua salinan kode tersebut untuk memastikan konsistensi.

# **Mengapa Duplikasi Kode Perlu Dihindari?**:
# 1. **Pemeliharaan yang Sulit**: Jika ada perubahan yang perlu dilakukan pada kode yang terduplikasi, 
# kita harus memperbarui setiap salinan kode tersebut, yang meningkatkan risiko kesalahan.
# 2. **Ukuran Kode yang Besar**: Duplikasi kode membuat kode program lebih panjang dan membingungkan.
# 3. **Kesalahan Potensial**: Duplikasi meningkatkan kemungkinan terjadinya bug jika ada ketidakkonsistenan antara salinan kode.

# **Cara Menghindari Duplikasi Kode**:
# Salah satu cara terbaik untuk menghindari duplikasi kode adalah dengan **membuat fungsi** untuk bagian kode yang sering digunakan.
# Fungsi memungkinkan kita untuk mengelompokkan kode yang berulang, membuatnya lebih modular, dan lebih mudah dipelihara.

# **Contoh Duplikasi Kode**:

# Misalkan kita memiliki dua fungsi yang melakukan tugas yang sangat mirip (misalnya, menghitung luas dua bentuk geometri):
def luas_persegi(panjang):
    return panjang * panjang

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Jika kita menambahkan fungsi lain dengan pola yang mirip, kita mulai melihat duplikasi kode.
# Untuk memperbaikinya, kita bisa membuat sebuah fungsi yang dapat menangani beberapa kasus.

# **Menghindari Duplikasi Kode dengan Fungsi Umum**:
# Daripada menulis kode duplikat, kita bisa membuat satu fungsi yang dapat digunakan untuk berbagai jenis perhitungan luas.

def hitung_luas(bentuk, *args):
    if bentuk == "persegi":
        return args[0] * args[0]  # Menghitung luas persegi
    elif bentuk == "persegi_panjang":
        return args[0] * args[1]  # Menghitung luas persegi panjang
    else:
        return "Bentuk tidak dikenal"

# Dengan satu fungsi, kita bisa menghitung luas berbagai bentuk tanpa menduplikasi kode.
# Memanggil fungsi untuk menghitung luas persegi
print(hitung_luas("persegi", 5))  # Output: 25

# Memanggil fungsi untuk menghitung luas persegi panjang
print(hitung_luas("persegi_panjang", 5, 10))  # Output: 50

# **Penjelasan**:
# - Fungsi 'hitung_luas' menerima dua parameter: 'bentuk' untuk menentukan jenis bentuk dan '*args' untuk menangani sejumlah argumen.
# - Fungsi ini hanya satu kali, tetapi dapat menangani berbagai jenis bentuk dengan cara yang lebih modular dan fleksibel.
# - Dengan menggunakan *args, kita bisa menangani banyak argumen tanpa perlu menulis banyak kode duplikat.

# **Menggunakan Kelas untuk Menghindari Duplikasi Kode**:
# Selain fungsi, kita juga dapat menggunakan konsep pemrograman berorientasi objek (OOP) untuk menghindari duplikasi kode.
# Misalnya, kita bisa membuat kelas untuk bentuk-bentuk geometri dan mendefinisikan metode di dalamnya.

class BentukGeometri:
    def hitung_luas(self):
        pass  # Ini akan di-overrided oleh kelas turunan

class Persegi(BentukGeometri):
    def __init__(self, panjang):
        self.panjang = panjang

    def hitung_luas(self):
        return self.panjang * self.panjang

class PersegiPanjang(BentukGeometri):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

# Membuat objek dari kelas-kelas tersebut dan memanggil metode hitung_luas()
persegi = Persegi(5)
print(persegi.hitung_luas())  # Output: 25

persegi_panjang = PersegiPanjang(5, 10)
print(persegi_panjang.hitung_luas())  # Output: 50

# **Penjelasan**:
# - Dengan menggunakan konsep kelas dan pewarisan, kita bisa mendefinisikan berbagai bentuk geometri tanpa menulis kode yang duplikat.
# - Setiap kelas (seperti Persegi dan PersegiPanjang) hanya perlu mendefinisikan cara menghitung luas sesuai dengan spesifikasi bentuk tersebut.
# - Dengan demikian, kita bisa menambahkan lebih banyak bentuk hanya dengan menambahkan kelas baru tanpa menulis ulang kode.

# **Menggunakan Modul untuk Menghindari Duplikasi**:
# Jika bagian kode yang digunakan berulang kali tersebar di beberapa bagian program, kita bisa menempatkannya dalam modul terpisah.
# Kemudian, modul tersebut bisa digunakan kembali tanpa menyalin kode.

# Contoh membuat modul geometri.py untuk menghitung luas:
# File geometri.py
def luas_persegi(panjang):
    return panjang * panjang

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Di file utama program kita, kita cukup mengimpor modul tersebut dan menggunakan fungsi yang sudah didefinisikan.
# Program utama.py
import geometri

print(geometri.luas_persegi(5))  # Output: 25
print(geometri.luas_persegi_panjang(5, 10))  # Output: 50

# **Kesimpulan**:
# - Menghindari duplikasi kode adalah praktik terbaik dalam pengembangan perangkat lunak.
# - Duplikasi kode meningkatkan kompleksitas dan potensi kesalahan.
# - Gunakan fungsi, kelas, dan modul untuk menghindari penulisan kode yang berulang.
# - Dengan menggunakan teknik-teknik ini, kode menjadi lebih modular, mudah dipelihara, dan lebih bersih.
