'''
Program yang menebak angka rahasia (antara 1–20).
Program akan meminta user menebak angka
Jika benar, cetak "Benar!" dan berhenti
Jika salah, beri petunjuk: “Terlalu kecil” atau “Terlalu besar”
Maksimal percobaan: 5 kali

Jika gagal menebak setelah 5 percobaan, tampilkan "Gagal menebak!"
'''
import random
rahasia = random.randint(1,10)
percobaan_maksimal = 5
percobaan_jumlah = 0
while percobaan_jumlah<percobaan_maksimal:
    tebakan = int(input(f"Tebakan ke-{percobaan_jumlah + 1}: "))
    percobaan_jumlah = percobaan_jumlah+1
    if tebakan<rahasia:
        print("Terlalu kecil!")
    elif tebakan==rahasia:
        print("Tebakan anda benar!")
        break
    else:
        print("Terlalu besar!")
if tebakan!=rahasia:
    print("Kesempatan Habis. Anda gagal!")
else:
    print("Anda lolos!")
        

