file_baru = "mynotes.txt"

def show_menu():
    print("----- Note App Menu -----")
    print("1. Add a new note")
    print("2. View All notes")
    print("3. Delete All notes")
    print("4. Exit")

def add_note():
    tambah = input("Enter a new note : ")
    with open(file_baru, "a") as file:
        file.write(tambah + "\n")
    print("Note added successfully")

def view_note():
    try:
        with open(file_baru, "r") as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("No notes found")
    except:
        print("No notes found")

def delete_notes():
    confirm = input("are you sure? y/n")
    if confirm.lower() == "y":
        with open(file_baru, "w") as file:
            pass
        print("Notes have been deleted")
    else: 
        print("Deletion cancelled")

while True:
    show_menu()
    pilihan = input("Masukkan pilihan :")
    if pilihan == "1":
        add_note()
    elif pilihan == "2":
        view_note()
    elif pilihan == "3":
        delete_notes()
    else:
        print("Terima kasih telah berkunjung")
        break