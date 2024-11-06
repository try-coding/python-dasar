# 3.4 Dictionary - Koleksi Pasangan Key-Value

# Membuat Dictionary
# Dictionary adalah koleksi yang berisi pasangan key-value. Setiap key harus unik, 
# dan nilai yang berhubungan (value) bisa berupa tipe data apapun.
person = {"nama": "John", "usia": 30, "kota": "Jakarta"}
print("Dictionary person:", person)

# Mengakses Nilai dari Dictionary
# Nilai dapat diakses menggunakan key.
print("Nama:", person["nama"])  # Mengakses nilai dengan key 'nama'
print("Usia:", person["usia"])  # Mengakses nilai dengan key 'usia'

# Jika key tidak ada, akan menimbulkan error (KeyError).
# print(person["pekerjaan"])  # Ini akan menimbulkan KeyError karena key 'pekerjaan' tidak ada.

# Menggunakan metode .get() untuk mengakses nilai
# .get() tidak menimbulkan error jika key tidak ada dan dapat memberi nilai default.
print("Pekerjaan:", person.get("pekerjaan", "Tidak diketahui"))  # Menggunakan get dengan nilai default

# Menambah atau Mengubah Nilai dalam Dictionary
# Jika key sudah ada, maka nilai akan diubah.
person["usia"] = 31  # Mengubah nilai 'usia' menjadi 31
print("Dictionary setelah mengubah usia:", person)

# Menambahkan pasangan key-value baru
person["pekerjaan"] = "Programmer"
print("Dictionary setelah menambahkan pekerjaan:", person)

# Menghapus elemen dari Dictionary
# Menggunakan metode .pop() untuk menghapus item berdasarkan key dan mendapatkan nilai yang dihapus.
removed_value = person.pop("kota")
print("Dictionary setelah menghapus kota:", person)
print("Nilai yang dihapus:", removed_value)

# Menggunakan metode .popitem() untuk menghapus pasangan key-value terakhir
removed_item = person.popitem()  # Menghapus pasangan key-value terakhir
print("Dictionary setelah popitem:", person)
print("Item yang dihapus:", removed_item)

# Menghapus seluruh elemen dalam dictionary
person.clear()
print("Dictionary setelah clear:", person)

# Menyaring Key dan Value
# Anda bisa mendapatkan semua keys, values, atau item (key-value pair) dengan metode .keys(), .values(), dan .items()
person = {"nama": "John", "usia": 31, "kota": "Jakarta", "pekerjaan": "Programmer"}

print("Keys (keys):", person.keys())  # Mengambil semua keys
print("Values (values):", person.values())  # Mengambil semua values
print("Items (key-value pairs):", person.items())  # Mengambil semua key-value pairs

# Menyaring hanya berdasarkan kunci tertentu
print("Nama hanya:", person.get("nama"))  # Mengambil value berdasarkan key 'nama'

# Menggunakan Operator Keanggotaan
# Menggunakan operator 'in' untuk memeriksa apakah suatu key ada dalam dictionary
print("'nama' ada dalam dictionary?", "nama" in person)  # True jika key 'nama' ada
print("'alamat' ada dalam dictionary?", "alamat" in person)  # False jika key 'alamat' tidak ada

# Mengonversi Dictionary ke List atau Tuple
# Mengonversi keys, values, atau item ke dalam list atau tuple
keys_list = list(person.keys())  # Mengonversi keys ke list
values_list = list(person.values())  # Mengonversi values ke list
items_list = list(person.items())  # Mengonversi items (key-value pair) ke list

print("Keys as list:", keys_list)
print("Values as list:", values_list)
print("Items as list:", items_list)
