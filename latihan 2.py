
# Program Daftar Nilai Mahasiswa Menggunakan Dictionary

mahasiswa = {}  # format: {nama: nilai_akhir}

def hitung_nilai_akhir(tugas, uts, uas):
    return (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)

def tambah_data():
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    mahasiswa[nama] = {
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Akhir": nilai_akhir
    }
    print(f"Data {nama} berhasil ditambahkan!\n")

def ubah_data():
    nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
    if nama in mahasiswa:
        print("Masukkan nilai baru:")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))

        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        mahasiswa[nama] = {
            "Tugas": tugas,
            "UTS": uts,
            "UAS": uas,
            "Akhir": nilai_akhir
        }
        print(f"Data {nama} berhasil diubah!\n")
    else:
        print("Data tidak ditemukan!\n")

def hapus_data():
    nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
    if nama in mahasiswa:
        del mahasiswa[nama]
        print(f"Data {nama} berhasil dihapus!\n")
    else:
        print("Data tidak ditemukan!\n")

def tampilkan_data():
    if not mahasiswa:
        print("Belum ada data!\n")
        return
    print("-" * 50)
    print("Daftar Nilai Mahasiswa")
    print("-" * 50)
    for nama, nilai in mahasiswa.items():
        print(f"Nama : {nama}")
        print(f"  Tugas : {nilai['Tugas']}")
        print(f"  UTS   : {nilai['UTS']}")
        print(f"  UAS   : {nilai['UAS']}")
        print(f"  Akhir : {nilai['Akhir']:.2f}")
        print("-" * 50)
    print()

def cari_data():
    nama = input("Masukkan nama mahasiswa yang dicari: ")
    if nama in mahasiswa:
        nilai = mahasiswa[nama]
        print(f"Data {nama}:")
        print(f"  Tugas : {nilai['Tugas']}")
        print(f"  UTS   : {nilai['UTS']}")
        print(f"  UAS   : {nilai['UAS']}")
        print(f"  Akhir : {nilai['Akhir']:.2f}\n")
    else:
        print("Data tidak ditemukan!\n")

# MENU UTAMA
while True:
    print("=== MENU PROGRAM NILAI MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        ubah_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        tampilkan_data()
    elif pilihan == "5":
        cari_data()
    elif pilihan == "0":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!\n")

