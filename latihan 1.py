# Buat Dictionary daftar kontak
kontak = {
    "Agus": "081267888",
    "Sulis": "087677776"
}

# Tampilkan kontaknya Agus
print("Kontak Agus:", kontak["Agus"])

# Tambah kontak baru Aldi
kontak["Aldi"] = "087654544"
print("Kontak setelah tambah Aldi:", kontak)

# Ubah kontak Sulis dengan nomor baru
kontak["Anggun"] = "088999776"
print("Kontak setelah update Anggun:", kontak)

# Tampilkan semua Nama
print("\nDaftar Nama:")
for nama in kontak.keys():
    print(nama)

# Tampilkan semua Nomor
print("\nDaftar Nomor:")
for nomor in kontak.values():
    print(nomor)

# Tampilkan daftar Nama dan nomornya
print("\nDaftar Kontak Lengkap:")
for nama, nomor in kontak.items():
    print(nama, ":", nomor)

# Hapus kontak Anggun
del kontak["Anggun"]
print("\nKontak setelah menghapus Anggun:", kontak)
