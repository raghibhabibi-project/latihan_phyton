'''
Program yang mencetak semua bilangan dari 1 sampai n,
tapi hanya tampilkan yang kelipatan 3 atau 5.
'''
n = int(input("Masukkan nomor : "))
for i in range(1,n+1):
    if i%3==0 or i%5==0:
        print(i)