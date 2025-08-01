daftar_buku = []
def tambah_buku(judul, pengarang):
    buku_baru = {"judul": judul, "pengarang": pengarang, "status": "Tersedia"}
    daftar_buku.append(buku_baru)
    print(f"Buku {judul} berhasil ditambahkan")

def cari_buku(kata_kunci):
    hasil_pencarian = []
    for buku in daftar_buku:
        if kata_kunci.lower() in buku["judul"].lower() or kata_kunci.lower() in buku["pengarang"].lower():
            hasil_pencarian.append(buku)
    if hasil_pencarian:
        print("Hasil pencarian:")
        for buku in hasil_pencarian:
            print(f"- {buku['judul']} oleh {buku['pengarang']} ({buku['status']})")
    else:
        print("Buku tidak ditemukan.")

def pinjam_buku(judul):
    for buku in daftar_buku:
        if buku["judul"].lower() == judul.lower():
            if buku["status"] == "Tersedia":
                buku["status"] = "Dipinjam"
                print(f"Buku '{judul}' berhasil dipinjam!")
                return
            else:
                print(f"Buku '{judul}' sedang tidak tersedia.")
                return
    print("Buku tidak ditemukan.")

def kembalikan_buku(judul):
    for buku in daftar_buku:
        if buku["judul"].lower() == judul.lower():
            if buku["status"] == "Dipinjam":
                buku["status"] = "Tersedia"
                print(f"Buku '{judul}' berhasil dikembalikan!")
                return
            else:
                print(f"Buku '{judul}' tidak sedang dipinjam.")
                return
    print("Buku tidak ditemukan.")
    
def tampilkan_semua_buku():
    if not daftar_buku:
        print("Belum ada buku di perpustakaan.")
        return
    print("Daftar Buku:")
    for i, buku in enumerate(daftar_buku, 1):
        print(f"{i}. {buku['judul']} - {buku['pengarang']} ({buku['status']})")

while True:
    print("\n=== Sistem Manajemen Perpustakaan ===")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan Buku")
    print("5. Tampilkan Semua Buku")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        judul = input("Masukkan judul: ")
        pengarang = input("Masukkan pengarang: ")
        tambah_buku(judul, pengarang)
    elif pilihan == "2":
        kata_kunci = input("Masukkan judul/pengarang: ")
        cari_buku(kata_kunci)
    elif pilihan == "3":
        judul = input("Masukkan judul buku yang ingin dipinjam: ")
        pinjam_buku(judul)
    elif pilihan == "4":
        judul = input("Masukkan judul buku yang ingin dikembalikan: ")
        kembalikan_buku(judul)
    elif pilihan == "5":
        tampilkan_semua_buku()
    elif pilihan == "6":
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
