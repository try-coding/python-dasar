# 4.1.2 Elif - Else If untuk Memeriksa Beberapa Kondisi

# Dalam struktur percabangan, kadang kita ingin memeriksa lebih dari satu kondisi.
# Di sinilah penggunaan **elif** (else if) sangat berguna untuk menangani beberapa kemungkinan kondisi.

# Struktur dasar penggunaan elif adalah sebagai berikut:
# 
# if kondisi_pertama:
#     # Eksekusi jika kondisi pertama benar
# elif kondisi_kedua:
#     # Eksekusi jika kondisi pertama salah dan kondisi kedua benar
# elif kondisi_ketiga:
#     # Eksekusi jika kondisi kedua salah dan kondisi ketiga benar
# else:
#     # Eksekusi jika semua kondisi sebelumnya salah

# Contoh:
x = 10

if x > 20:
    print("x lebih besar dari 20")
elif x == 10:
    # Kondisi pertama (x > 20) salah, tapi kondisi kedua (x == 10) benar.
    print("x sama dengan 10")
elif x < 5:
    print("x kurang dari 5")
else:
    print("Tidak ada kondisi yang terpenuhi")

# Output:
# x sama dengan 10
# Karena kondisi pertama dan kedua tidak terpenuhi, tetapi kondisi kedua (x == 10) benar.

# **Penjelasan:**
# - Pada contoh di atas, kita pertama kali memeriksa apakah x lebih besar dari 20. 
#   Jika tidak benar, kita lanjut memeriksa apakah x sama dengan 10 menggunakan elif. 
#   Jika x sama dengan 10, maka program akan mengeksekusi kode dalam blok elif.
#   Jika tidak ada kondisi yang terpenuhi, maka bagian else akan dijalankan.

# Contoh lain dengan lebih dari dua kondisi:
nilai = 85

if nilai >= 90:
    print("Grade: A")
elif nilai >= 80:
    # Kondisi pertama (nilai >= 90) salah, tapi kondisi kedua (nilai >= 80) benar.
    print("Grade: B")
elif nilai >= 70:
    print("Grade: C")
elif nilai >= 60:
    print("Grade: D")
else:
    print("Grade: E")

# Output:
# Grade: B
# Program akan memeriksa secara berurutan apakah nilai lebih besar atau sama dengan 90, 
# kemudian 80, dan seterusnya. Setelah menemukan kondisi yang benar (nilai >= 80),
# program menampilkan "Grade: B".

# Penggunaan elif sangat berguna untuk menangani beberapa kondisi yang saling eksklusif
# (hanya satu kondisi yang bisa benar). Tidak perlu menggunakan banyak if yang terpisah,
# yang bisa mengakibatkan pemeriksaan kondisi yang tidak efisien dan membingungkan.

# Contoh dengan kondisi yang lebih kompleks:
hari = "Sabtu"

if hari == "Senin":
    print("Hari pertama dalam minggu kerja")
elif hari == "Selasa":
    print("Hari kedua dalam minggu kerja")
elif hari == "Sabtu":
    # Kondisi pertama (hari == "Senin") dan kedua (hari == "Selasa") salah,
    # tetapi kondisi ketiga (hari == "Sabtu") benar.
    print("Hari libur")
else:
    print("Hari lainnya")

# Output:
# Hari libur
# Program memeriksa urutan kondisi dengan menggunakan elif, 
# dan ketika menemukan kondisi yang sesuai (hari == "Sabtu"), 
# maka mengeksekusi bagian kode yang sesuai.

# **Catatan penting:**
# - Elif sangat berguna jika kita ingin memeriksa beberapa kondisi dalam urutan yang jelas.
# - Elif memungkinkan kita menghindari penggunaan banyak if yang bisa membingungkan dan kurang efisien.
# - Jika tidak ada kondisi yang benar, maka blok else akan dieksekusi (jika ada).
