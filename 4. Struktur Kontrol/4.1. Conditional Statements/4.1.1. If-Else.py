# 4.1.1 If-Else - Struktur Percabangan

# Menggunakan struktur if-else untuk mengambil keputusan berdasarkan kondisi.

# Misalnya, kita ingin memeriksa apakah sebuah angka lebih besar dari 0:
x = 5

# Jika kondisi x > 0 benar, maka blok kode di bawah if akan dijalankan.
if x > 0:
    print("x lebih besar dari 0")
else:
    # Jika kondisi x > 0 salah (x tidak lebih besar dari 0), maka blok kode di bawah else akan dijalankan.
    print("x tidak lebih besar dari 0")

# Contoh lain dengan beberapa kondisi menggunakan elif (else if)
# Menggunakan elif untuk memeriksa kondisi lain jika kondisi if sebelumnya salah.

y = -3

if y > 0:
    print("y lebih besar dari 0")
elif y == 0:
    # Jika y tidak lebih besar dari 0, periksa apakah y sama dengan 0.
    print("y sama dengan 0")
else:
    # Jika kondisi y > 0 dan y == 0 salah, maka yang tersisa adalah kondisi y < 0.
    print("y kurang dari 0")

# Contoh menggunakan operator logika and
# Kita ingin memeriksa apakah dua kondisi benar secara bersamaan:
a = 10
b = 20

if a > 5 and b > 15:
    print("a lebih besar dari 5 dan b lebih besar dari 15")
else:
    print("Salah satu atau kedua kondisi tidak terpenuhi")

# Contoh menggunakan operator logika or
# Menggunakan or untuk memeriksa apakah salah satu dari dua kondisi benar.
c = 3
d = 7

if c < 5 or d > 10:
    print("Salah satu kondisi benar, c < 5 atau d > 10")
else:
    print("Kedua kondisi salah")

# Contoh menggunakan operator logika not
# Menggunakan not untuk membalikkan kondisi
e = 12

if not e < 10:
    print("e tidak lebih kecil dari 10")
else:
    print("e lebih kecil dari 10")

# Nested if: Menggunakan if di dalam if
# Memeriksa lebih dari satu kondisi bertingkat.
f = 7

if f > 0:
    print("f lebih besar dari 0")
    if f < 10:
        print("f juga lebih kecil dari 10")
    else:
        print("f lebih besar atau sama dengan 10")
else:
    print("f kurang dari atau sama dengan 0")

# Membandingkan nilai dengan operator pembanding seperti ==, !=, <, >, <=, dan >=
g = 18

if g >= 18:
    print("Anda sudah dewasa")
else:
    print("Anda masih di bawah umur")

# Menambahkan kondisi if yang lebih sederhana
# Jika tidak menggunakan else, maka hanya kondisi if yang dieksekusi jika benar.
h = 8

if h % 2 == 0:  # Memeriksa apakah h adalah angka genap
    print("h adalah angka genap")

# Penjelasan singkat:
# - Struktur if-else memungkinkan kita membuat keputusan dalam program berdasarkan kondisi tertentu.
# - Jika kondisi pertama (if) benar, blok kode di dalam if dijalankan. Jika tidak, blok kode dalam else yang dijalankan.
# - elif digunakan untuk memeriksa beberapa kondisi secara berurutan.
# - Operator logika (and, or, not) membantu menggabungkan atau membalikkan kondisi.
# - Nested if memungkinkan kita memeriksa kondisi dalam kondisi lainnya.
