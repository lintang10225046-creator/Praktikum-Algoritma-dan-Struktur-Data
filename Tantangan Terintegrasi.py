
# Program Rekap Nilai Mahasiswa

nama = "Lintang"

# Pengujian pertama
nilai_tugas = 80
nilai_ujian = 90

rata_rata = (nilai_tugas + nilai_ujian) / 2
lulus = rata_rata >= 75

print("=== Pengujian Pertama ===")
print("Nama mahasiswa:", nama)
print("Nilai tugas:", nilai_tugas)
print("Nilai ujian:", nilai_ujian)
print("Rata-rata:", rata_rata)
print("Status lulus:", lulus)

# Pengujian kedua
nilai_tugas = 60
nilai_ujian = 70

rata_rata = (nilai_tugas + nilai_ujian) / 2
lulus = rata_rata >= 75

print("\n=== Pengujian Kedua ===")
print("Nama mahasiswa:", nama)
print("Nilai tugas:", nilai_tugas)
print("Nilai ujian:", nilai_ujian)
print("Rata-rata:", rata_rata)
print("Status lulus:", lulus)
