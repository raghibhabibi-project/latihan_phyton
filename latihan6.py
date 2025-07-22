import csv
list = ["Nama", "Umur", "Asal"]
datadic = [
    {"Nama" : "Andi", "Umur" : "30", "Asal" : "Jogja"},
    {"Nama" : "Budi", "Umur" : "35", "Asal" : "Solo"},
    {"Nama" : "Burhan", "Umur" : "25", "Asal" : "Bogor"}
    ]
with open("data2.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=list)      
    writer.writeheader()
    writer.writerows(datadic)

