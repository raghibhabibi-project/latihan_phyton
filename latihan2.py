'''
Program yang meminta input n
Lalu tampilkan semua bilangan dari 1 sampai n.
Tapi:
- Jika angka habis dibagi 3, tampilkan "Fizz"
- Jika habis dibagi 5, tampilkan "Buzz"
- Jika habis dibagi keduanya, tampilkan "FizzBuzz"
Selain itu, tampilkan angkanya sendiri
'''
n = int(input("Masukkan nomor : "))
for i in range(1, n+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)