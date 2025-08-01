resep = {"tepung", "gula", "mentega", "telur", "susu"}

user_input = input("Masukkan bahan yang anda punya (pisah dengan koma) : ")
user_bahan = set(user_input.split(", "))

missing_resep = resep - user_bahan
extra_resep = user_bahan - resep

print("-----resep checker results-----")
if missing_resep:
    print(f"Perlu bahan berikut : {', '.join(missing_resep)}")
else:
    print("Bahan lengkap. Siap menggoreng")

if extra_resep:
    print(f"Kelebihan bahan berikut : {', '.join(extra_resep)}")
else:
    print("tidak ada bahan berlebih.")
