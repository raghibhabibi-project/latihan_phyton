import csv
peserta_nama = []
peserta_umur = []
peserta_asal = []
def tampilan_menu():
    print("== Program Pendataan Peserta Workshop ==")
    print("1. Tambah Peserta")
    print("2. Tampilkan Peserta")
    print("3. Simpan Data ke CSV")
    print("4. Baca Data dari CSV")
    print("5. Keluar")
def tambah_peserta():
    nama = input("Nama :")
    umur = input("Umur :")
    asal = input("Asal :")
    peserta_nama.append(nama)
    peserta_umur.append(umur)
    peserta_asal.append(asal)
def tampilkan_peserta():
    print("\nDaftar Peserta: ")
    jumlah = len(nama)
    if jumlah == 0:
        print("Belum ada peserta terdaftar")
    else:
        for i in range(jumlah):
            print(f"{i+1}. Nama: {peserta_nama[i]}, Umur: {peserta_umur[i]}, Asal: {peserta_asal{i}}")
    