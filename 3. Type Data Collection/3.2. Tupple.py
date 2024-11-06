# 3.2 Tuple - Koleksi Terurut yang Tidak Dapat Diubah (Immutable)

# Membuat Tuple
# Tuple adalah koleksi terurut yang tidak dapat diubah (immutable). Berikut cara membuat tuple:
fruits_tuple = ("apel", "pisang", "ceri", "kurma")
print("Tuple buah:", fruits_tuple)

# Tuple juga bisa berisi berbagai tipe data:
mixed_tuple = (1, 3.14, "halo", True)
print("Tuple campuran:", mixed_tuple)

# Tuple kosong:
empty_tuple = ()
print("Tuple kosong:", empty_tuple)

# Tuple dengan satu elemen
# Jika hanya ada satu elemen, perlu menambahkan koma setelah elemen untuk membedakannya dari tipe data lain.
single_element_tuple = (5,)
print("Tuple dengan satu elemen:", single_element_tuple)

# Mengakses elemen dalam Tuple
# Akses elemen berdasarkan indeks (indeks dimulai dari 0)
print("Buah pertama dalam tuple:", fruits_tuple[0])  # Mengakses elemen pertama (indeks 0)

# Akses elemen dengan indeks negatif (dari belakang)
print("Buah terakhir dalam tuple:", fruits_tuple[-1])  # Mengakses elemen terakhir (-1)

# Menggunakan slicing untuk mengambil bagian dari tuple
print("Dua buah pertama dalam tuple:", fruits_tuple[:2])  # Mengambil elemen dari indeks 0 hingga 1
print("Dua buah terakhir dalam tuple:", fruits_tuple[-2:])  # Mengambil dua elemen terakhir

# Menampilkan panjang Tuple
print("Panjang tuple buah:", len(fruits_tuple))

# Tuple tidak dapat diubah (immutable)
# Contoh mencoba mengubah elemen tuple (akan menyebabkan error):
try:
    fruits_tuple[0] = "mangga"  # Mencoba mengubah elemen pertama
except TypeError as e:
    print("Error saat mencoba mengubah tuple:", e)

# Menyambung Tuple
# Anda dapat menggabungkan dua tuple menggunakan operator +
new_fruits_tuple = fruits_tuple + ("kiwi", "mangga")
print("Tuple baru setelah digabung:", new_fruits_tuple)

# Mengulang elemen dalam tuple menggunakan operator *
repeated_tuple = fruits_tuple * 2
print("Tuple yang diulang:", repeated_tuple)

# Menggunakan operator keanggotaan untuk memeriksa elemen
print("'apel' ada dalam tuple:", "apel" in fruits_tuple)  # True jika 'apel' ada dalam tuple
print("'anggur' ada dalam tuple:", "anggur" in fruits_tuple)  # False karena 'anggur' tidak ada

# Mengubah Tuple menjadi List
# Karena tuple bersifat immutable, jika ingin memodifikasi isinya, kita perlu mengonversinya ke list
fruits_list = list(fruits_tuple)
fruits_list.append("jeruk")
print("Tuple setelah diubah menjadi list dan ditambah jeruk:", fruits_list)

# Membuat Tuple dari List
# Sebaliknya, jika ingin mengonversi list kembali ke tuple, kita bisa menggunakan fungsi tuple()
new_tuple = tuple(fruits_list)
print("List setelah diubah kembali menjadi tuple:", new_tuple)
