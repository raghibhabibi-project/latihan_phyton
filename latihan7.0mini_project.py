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
    jumlah = len(peserta_nama)
    if jumlah == 0:
        print("Belum ada peserta terdaftar")
    else:
        for i in range(jumlah):
            print(f"{i+1}. Nama: {peserta_nama[i]} - Umur: {peserta_umur[i]} - Asal: {peserta_asal[i]}")
def simpan_csv():
    with open("peserta_workshop.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Nama", "Umur", "Asal"])
        for i in range(len(peserta_nama)):
            writer.writerow([peserta_nama[i], peserta_umur[i], peserta_asal[i]])
            print("Data Peserta Berhasil Disimpan")
def baca_csv():
        with open("peserta_workshop.csv", "r", newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                peserta_nama.append(row[0])
                peserta_umur.append(row[1])
                peserta_asal.append(row[2])
            print("Data berhasil dibaca")
while True:
    tampilan_menu()
    pilihan = int(input("Pilih menu : "))
    if pilihan == "1":
        tambah_peserta()
    elif pilihan == "2":
        tampilkan_peserta()
    elif pilihan == "3":
        simpan_csv()
    elif pilihan == "4":
        baca_csv()
    elif pilihan == "0":
        print("Terima kasih telah berkunjung")
        break
    else:
        print("Pilihan tidak valid. Coba lagi!")