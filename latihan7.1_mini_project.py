import pandas as pd

peserta_nama = []
peserta_umur = []
peserta_asal = []

def tampilan_menu():
    print("== Program Pendataan Peserta Workshop ==")
    print("1. Tambah Peserta")
    print("2. Tampilkan Peserta")
    print("3. Simpan Data ke CSV")
    print("4. Baca Data dari CSV")
    print("0. Keluar")

def tambah_peserta():
    nama = input("Nama :")
    umur = input("Umur :")
    asal = input("Asal :")
    peserta_nama.append(nama)
    peserta_umur.append(umur)
    peserta_asal.append(asal)

def tampilkan_peserta():
    print("\nDaftar Peserta: ")
    jumlah = len(peserta_nama)
    if jumlah == 0:
        print("Belum ada peserta terdaftar")
    else:
        for i in range(jumlah):
            print(f"{i+1}. Nama: {peserta_nama[i]} - Umur: {peserta_umur[i]} - Asal: {peserta_asal[i]}")

def simpan_csv():
    data_csv = pd.DataFrame({
        "Nama" : peserta_nama,
        "Umur" : peserta_umur,
        "Asal" : peserta_asal
    })
    data_csv.to_csv("peserta_workshop.csv", index=False, encoding='utf-8')
    print("Data peserta telah disimpan ke 'peserta_workshop.csv'")

def baca_csv():
    try:
        df = pd.read_csv("peserta_workshop.csv")
        peserta_nama.clear()
        peserta_umur.clear()
        peserta_asal.clear()
        for i, row in df.iterrows():
            peserta_nama.append(row['Nama'])
            peserta_umur.append(row['Umur'])
            peserta_asal.append(row['Asal'])
        print("Data peserta telah dibaca dari 'peserta_workshop.csv'")
    except FileNotFoundError:
        print("File tidak ditemukan")
while True:
    tampilan_menu()
    pilihan = int(input("Pilih menu : "))
    if pilihan == 1:
        tambah_peserta()
    elif pilihan == 2:
        tampilkan_peserta()
    elif pilihan == 3:
        simpan_csv()
    elif pilihan == 4:
        baca_csv()
    elif pilihan == 0:
        print("Terima kasih telah berkunjung")
        break
    else:
        print("Pilihan tidak valid. Coba lagi!")