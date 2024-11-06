# 4.2.2 While Loop - Perulangan dengan Kondisi

# While loop adalah jenis perulangan yang akan terus berjalan selama kondisi yang diberikan bernilai True.
# Selama kondisi tersebut masih benar (True), blok kode di dalam while loop akan terus dieksekusi.
# Jika kondisi menjadi False, maka perulangan akan berhenti.

# **Struktur dasar while loop**:
# while kondisi:
#     # Blok kode yang akan dieksekusi selama kondisi bernilai True

# Contoh 1: While loop sederhana
count = 0

while count < 5:
    # Selama count kurang dari 5, blok kode ini akan dijalankan
    print("Count:", count)
    count += 1  # Menambahkan 1 ke count pada setiap iterasi

# Output:
# Count: 0
# Count: 1
# Count: 2
# Count: 3
# Count: 4

# **Penjelasan:**
# - Di sini, while loop akan terus berjalan selama nilai 'count' lebih kecil dari 5.
# - Pada setiap iterasi, 'count' akan ditambah 1, sehingga ketika count mencapai 5, kondisi (count < 5) menjadi False dan perulangan berhenti.

# Contoh 2: Menggunakan while loop dengan kondisi yang berubah di dalam perulangan
# Menggunakan while loop untuk meminta input dari pengguna sampai pengguna memberikan input yang benar.

user_input = ""

while user_input != "exit":
    # Meminta input dari pengguna untuk keluar dari perulangan
    user_input = input("Ketik 'exit' untuk keluar: ")
    print("Anda mengetik:", user_input)

# Jika pengguna mengetik "exit", while loop akan berhenti.

# **Penjelasan:**
# - Program meminta input pengguna dalam setiap iterasi.
# - Perulangan akan terus berlanjut selama input bukan "exit".
# - Setelah pengguna mengetik "exit", kondisi menjadi False dan perulangan berhenti.

# Contoh 3: Menggunakan while dengan kondisi lebih kompleks
# Menyusun perulangan untuk menghitung faktorial dari sebuah angka.

number = 5
faktorial = 1
i = 1

while i <= number:
    faktorial *= i  # Kalikan nilai faktorial dengan i pada setiap iterasi
    i += 1  # Menambah nilai i setiap iterasi

print(f"Faktorial dari {number} adalah {faktorial}")

# Output:
# Faktorial dari 5 adalah 120
# Penjelasan:
# - Faktorial dihitung dengan mengalikan angka dari 1 sampai 5, yaitu: 1 * 2 * 3 * 4 * 5 = 120.
# - Perulangan berhenti setelah i menjadi lebih besar dari 5 (i > 5).

# Contoh 4: Menggunakan break untuk keluar dari perulangan
# Kita bisa menggunakan pernyataan `break` untuk keluar dari perulangan secara paksa saat kondisi tertentu terpenuhi.

i = 0

while True:
    # Perulangan terus berjalan karena kondisi True selalu terpenuhi
    i += 1
    print(i)
    if i == 5:
        print("Menghentikan perulangan dengan break")
        break  # Keluar dari perulangan jika i mencapai 5

# Output:
# 1
# 2
# 3
# 4
# 5
# Menghentikan perulangan dengan break
# Penjelasan:
# - Di sini, kita menggunakan while loop dengan kondisi `True`, yang artinya perulangan akan terus berjalan tanpa henti.
# - Namun, setelah nilai i mencapai 5, perintah `break` dieksekusi, menghentikan perulangan secara paksa.

# Contoh 5: Menggunakan continue untuk melanjutkan perulangan tanpa menjalankan sisa kode
# Perintah `continue` digunakan untuk melewati sisa kode dalam perulangan dan langsung melanjutkan ke iterasi berikutnya.

j = 0

while j < 5:
    j += 1
    if j == 3:
        # Jika j == 3, skip sisa kode dan lanjutkan ke iterasi berikutnya
        continue
    print(f"Nilai j adalah {j}")

# Output:
# Nilai j adalah 1
# Nilai j adalah 2
# Nilai j adalah 4
# Nilai j adalah 5
# Penjelasan:
# - Ketika nilai j mencapai 3, perintah `continue` men-skip perintah print dan langsung melanjutkan ke iterasi berikutnya.
# - Dengan demikian, nilai 3 tidak akan dicetak.

# **Catatan tentang While Loop**:
# - **Kondisi** dalam while loop adalah ekspresi yang harus bernilai True atau False.
# - Selama kondisi bernilai True, perulangan akan terus berlangsung.
# - Jika kondisi bernilai False, perulangan akan berhenti.
# - **Break** digunakan untuk keluar dari perulangan lebih awal.
# - **Continue** digunakan untuk melewati iterasi saat ini dan melanjutkan ke iterasi berikutnya.
# - Pastikan untuk mengubah kondisi dalam perulangan (misalnya dengan menambah variabel) agar perulangan tidak menjadi infinite (perulangan yang tidak pernah berhenti).
