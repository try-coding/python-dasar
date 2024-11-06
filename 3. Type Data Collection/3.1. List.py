# 3.1 List - Koleksi Terurut yang Dapat Diubah (Mutable)

# Membuat List
# List adalah koleksi terurut dan bisa diubah (mutable). Berikut cara membuat list:
fruits = ["apel", "pisang", "ceri", "kurma"]
print("Daftar buah:", fruits)

# List juga bisa berisi berbagai tipe data:
mixed_list = [1, 3.14, "halo", True]
print("List campuran:", mixed_list)

# List kosong:
empty_list = []
print("List kosong:", empty_list)

# Menambah elemen ke dalam List
# Menggunakan metode .append() untuk menambahkan elemen di akhir list
fruits.append("anggur")
print("Daftar buah setelah ditambahkan anggur:", fruits)

# Menambah elemen di posisi tertentu dengan .insert()
fruits.insert(2, "kiwi")  # Menambahkan 'kiwi' di posisi indeks 2
print("Daftar buah setelah ditambahkan kiwi di posisi 2:", fruits)

# Menghapus elemen dari List
# Menggunakan metode .remove() untuk menghapus elemen pertama yang ditemukan
fruits.remove("pisang")
print("Daftar buah setelah menghapus 'pisang':", fruits)

# Menghapus elemen berdasarkan indeks menggunakan .pop()
removed_item = fruits.pop(1)  # Menghapus item di indeks 1
print("Daftar buah setelah pop:", fruits)
print("Elemen yang dihapus:", removed_item)

# Menghapus seluruh elemen dalam list
fruits.clear()
print("Daftar buah setelah dihapus semua:", fruits)

# Mengakses elemen dalam List
# Akses elemen berdasarkan indeks (indeks dimulai dari 0)
fruits = ["apel", "pisang", "ceri", "kurma"]
print("Buah pertama:", fruits[0])  # Mengakses elemen pertama (indeks 0)

# Akses elemen dengan indeks negatif (dari belakang)
print("Buah terakhir:", fruits[-1])  # Mengakses elemen terakhir (-1)

# Menggunakan slicing untuk mengambil bagian dari list
print("Dua buah pertama:", fruits[:2])  # Mengambil elemen dari indeks 0 hingga 1
print("Dua buah terakhir:", fruits[-2:])  # Mengambil dua elemen terakhir

# Menampilkan panjang List
print("Panjang daftar buah:", len(fruits))

# Menggunakan Operator
# Menambahkan dua list menggunakan operator +
new_fruits = fruits + ["kiwi", "mangga"]
print("Daftar buah baru:", new_fruits)

# Mengulangi elemen dalam list menggunakan operator *
repeated_fruits = fruits * 2
print("Daftar buah yang diulang:", repeated_fruits)

# Menggunakan operator keanggotaan untuk memeriksa elemen
print("'apel' ada dalam daftar buah:", "apel" in fruits)  # True jika 'apel' ada dalam list
print("'anggur' ada dalam daftar buah:", "anggur" in fruits)  # False karena 'anggur' tidak ada

# Menyortir List
# Menggunakan metode .sort() untuk mengurutkan elemen dalam list (modifikasi in-place)
numbers = [4, 1, 3, 9, 2]
numbers.sort()
print("Angka yang telah diurutkan:", numbers)

# Untuk membalik urutan list, gunakan reverse()
numbers.reverse()
print("Angka setelah dibalik:", numbers)

# Membuat salinan dari List
# Menggunakan metode .copy() untuk menyalin list
fruits_copy = fruits.copy()
print("Salinan daftar buah:", fruits_copy)

# List dalam List (Nested List)
# List bisa berisi list lainnya (nested lists)
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("List bersarang:", nested_list)

# Mengakses elemen dalam nested list
print("List pertama dalam nested list:", nested_list[0])  # Mengakses list pertama
print("Elemen dari list kedua dalam nested list:", nested_list[1][2])  # Mengakses elemen kedua dari list kedua
