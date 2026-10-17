# 1. Buat variabel harga dan jumlah
harga = 12500
jumlah = 4

# 2. Hitung total harga
total_harga = harga * jumlah

# 3. Hitung sisa pembagian total harga dengan 2.000 menggunakan operator %
sisa_pembagian = total_harga % 2000

# 4. Hitung harga setelah diskon Rp5.000
harga_setelah_diskon = total_harga - 5000

# 5. Tampilkan hasil dengan tanda koma ( , )
print("Harga per buku       : Rp", harga)
print("Jumlah buku dibeli   :", jumlah, "buah")
print("Total harga          : Rp", total_harga)
print("Sisa pembagian % 2000: Rp", sisa_pembagian)
print("Harga setelah diskon : Rp", harga_setelah_diskon)