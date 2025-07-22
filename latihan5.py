import csv
list = ["Nama", "Umur", "Asal"]
datalist = [["andi", "30", "Jogja"], ["Budi", "35", "Solo"],["Burhan", "25", "Bogor"]]
with open("data.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(list)
    writer.writerows(datalist)
    