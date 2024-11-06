# 3.3 Set - Koleksi Tidak Terurut dan Tidak Mengizinkan Duplikasi

# Membuat Set
# Set adalah koleksi tidak terurut dan tidak mengizinkan elemen yang duplikat.
# Berikut cara membuat set:
fruits_set = {"apel", "pisang", "ceri", "kurma"}
print("Set buah:", fruits_set)

# Set juga bisa berisi berbagai tipe data:
mixed_set = {1, 3.14, "halo", True}
print("Set campuran:", mixed_set)

# Set kosong:
empty_set = set()  # Set kosong harus dibuat dengan menggunakan fungsi set(), bukan {}
print("Set kosong:", empty_set)

# Menambah elemen ke dalam Set
# Menggunakan metode .add() untuk menambahkan elemen baru
fruits_set.add("kiwi")
print("Set buah setelah ditambahkan kiwi:", fruits_set)

# Menghapus elemen dari Set
# Menggunakan metode .remove() untuk menghapus elemen yang ada di dalam set
fruits_set.remove("pisang")
print("Set buah setelah menghapus pisang:", fruits_set)

# Menghapus elemen dengan metode .discard() (tidak menimbulkan error jika elemen tidak ada)
fruits_set.discard("anggur")  # Tidak akan menyebabkan error meskipun 'anggur' tidak ada dalam set
print("Set buah setelah mencoba menghapus anggur:", fruits_set)

# Menghapus elemen secara acak menggunakan .pop()
removed_item = fruits_set.pop()  # Menghapus elemen acak (karena set tidak terurut)
print("Set buah setelah pop:", fruits_set)
print("Elemen yang dihapus:", removed_item)

# Menghapus seluruh elemen dalam set
fruits_set.clear()
print("Set buah setelah dihapus semua:", fruits_set)

# Menggunakan Operator
# Menambahkan dua set menggunakan operator union (|) atau metode .union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Gabungkan dua set, hasilnya hanya elemen unik
print("Union set (gabungan set1 dan set2):", union_set)

# Menghitung irisan dua set menggunakan operator intersection (&) atau metode .intersection()
intersection_set = set1 & set2  # Mengambil elemen yang ada di kedua set
print("Intersection set (irisan set1 dan set2):", intersection_set)

# Menghitung selisih dua set menggunakan operator difference (-) atau metode .difference()
difference_set = set1 - set2  # Mengambil elemen yang ada di set1 tetapi tidak ada di set2
print("Difference set (selisih set1 dan set2):", difference_set)

# Menggunakan operator keanggotaan untuk memeriksa elemen
print("'apel' ada dalam set?", "apel" in fruits_set)  # False karena set kosong
print("'kiwi' ada dalam union_set?", "kiwi" in union_set)  # False karena 'kiwi' tidak ada dalam union_set

# Menyortir Set
# Set tidak terurut secara langsung, tetapi kita bisa mengurutkan elemen set dengan mengubahnya menjadi list.
sorted_set = sorted(set1)
print("Set1 yang disortir:", sorted_set)

# Set dalam Set (Nested Set)
# Set bisa berisi set lain, tetapi set dalam set harus bersifat immutable (frozen set).
nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print("Set bersarang:", nested_set)

# Mengonversi Set ke List atau Tuple
# Anda dapat mengonversi set ke list atau tuple jika ingin mengubahnya menjadi koleksi terurut
set_as_list = list(set1)
set_as_tuple = tuple(set1)
print("Set sebagai List:", set_as_list)
print("Set sebagai Tuple:", set_as_tuple)
