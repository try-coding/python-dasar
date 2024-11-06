# 5.2 Parameter dan Argumen - Memahami Perbedaan dan Penggunaannya dalam Fungsi

# Dalam Python, fungsi dapat menerima data melalui *parameter* dan *argumen*.
# Parameter adalah nama yang digunakan untuk merujuk ke data yang diterima oleh fungsi.
# Argumen adalah nilai yang diberikan pada saat fungsi dipanggil yang cocok dengan parameter yang ada.

# **Definisi Parameter**:
# - Parameter adalah variabel yang didefinisikan dalam tanda kurung saat kita mendefinisikan fungsi.
# - Parameter digunakan untuk menerima input yang diperlukan oleh fungsi.

# **Definisi Argumen**:
# - Argumen adalah nilai yang kita berikan saat memanggil fungsi.
# - Nilai ini akan dipetakan ke parameter yang sesuai dalam fungsi yang dipanggil.

# **Contoh 1: Fungsi dengan satu parameter**
# Fungsi ini menerima satu parameter, yaitu 'nama', dan mencetak sapaan.
def sapa(nama):
    print(f"Halo, {nama}! Selamat datang di Python.")

# Memanggil fungsi dengan memberikan argumen (nilai untuk parameter)
sapa("Andi")  # Output: Halo, Andi! Selamat datang di Python.

# **Penjelasan:**
# - Parameter 'nama' digunakan untuk menerima nilai yang diberikan ketika fungsi dipanggil.
# - Argumen yang diberikan adalah 'Andi', yang akan digunakan dalam fungsi sebagai nilai untuk parameter 'nama'.

# **Contoh 2: Fungsi dengan dua parameter**
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}.")

# Memanggil fungsi dengan dua argumen
hitung_luas(10, 5)  # Output: Luas persegi panjang dengan panjang 10 dan lebar 5 adalah 50.

# **Penjelasan:**
# - Fungsi 'hitung_luas' memiliki dua parameter: 'panjang' dan 'lebar'.
# - Ketika memanggil fungsi, kita memberikan dua argumen, yaitu 10 dan 5, yang dipetakan ke parameter 'panjang' dan 'lebar'.

# **Contoh 3: Fungsi dengan parameter default**
# Fungsi ini memiliki parameter dengan nilai default yang akan digunakan jika argumen tidak diberikan.
def sapa_default(nama="Tamu"):
    print(f"Halo, {nama}! Selamat datang di Python.")

# Memanggil fungsi tanpa memberikan argumen (akan menggunakan nilai default)
sapa_default()  # Output: Halo, Tamu! Selamat datang di Python.

# Memanggil fungsi dengan memberikan argumen
sapa_default("Budi")  # Output: Halo, Budi! Selamat datang di Python.

# **Penjelasan:**
# - Parameter 'nama' pada fungsi 'sapa_default' memiliki nilai default "Tamu". 
# - Jika kita tidak memberikan argumen saat memanggil fungsi, nilai default ini yang akan digunakan.

# **Contoh 4: Fungsi dengan argumen variabel (*args)**
# Fungsi ini menerima sejumlah argumen yang tidak terbatas.
def jumlahkan_semua(*args):
    total = sum(args)
    print(f"Jumlah semua angka: {total}")

# Memanggil fungsi dengan sejumlah argumen
jumlahkan_semua(1, 2, 3)  # Output: Jumlah semua angka: 6
jumlahkan_semua(10, 20, 30, 40)  # Output: Jumlah semua angka: 100

# **Penjelasan:**
# - Dengan menggunakan *args, fungsi dapat menerima sejumlah argumen yang tidak terbatas.
# - 'args' di dalam fungsi adalah tuple yang berisi semua argumen yang diberikan.

# **Contoh 5: Fungsi dengan keyword arguments (**kwargs)**
# Fungsi ini dapat menerima sejumlah pasangan key-value (keyword arguments).
def tampilkan_data(**kwargs):
    for kunci, nilai in kwargs.items():
        print(f"{kunci}: {nilai}")

# Memanggil fungsi dengan keyword arguments
tampilkan_data(nama="Andi", umur=25, pekerjaan="Programmer")
# Output:
# nama: Andi
# umur: 25
# pekerjaan: Programmer

# **Penjelasan:**
# - Dengan **kwargs, fungsi dapat menerima pasangan key-value (keyword arguments).
# - 'kwargs' adalah dictionary yang berisi semua pasangan key-value yang diberikan.

# **Kesimpulan:**
# - **Parameter** adalah nama yang digunakan dalam definisi fungsi untuk merujuk pada data yang akan diterima.
# - **Argumen** adalah nilai yang diberikan pada saat pemanggilan fungsi yang sesuai dengan pa
