def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    if y == 0:
        raise ZeroDivisionError("Ga boleh 0")
    return x/y

def show_menu():
    print("----- Calculator App Menu -----")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")

while True:
    show_menu()
    pilihan = input("Masukkan pilihan (1-5): ")
    
    if pilihan == "5":
        print("Terima kasih telah berkunjung")
        break
    elif pilihan not in ["1", "2", "3", "4"]:
        print("Input tidak valid! Harap masukkan angka 1-5")
        continue  
     
    try:
        num1 = float(input("Enter the first number : "))
        num2 = float(input("Enter the second number : "))

        if pilihan == "1":
            print("Result : ", add(num1,num2)) 
        elif pilihan == "2":
            print("Result : ", substract(num1,num2)) 
        elif pilihan == "3":
            print("Result : ", multi(num1,num2)) 
        elif pilihan == "4":
            print("Result : ", div(num1,num2)) 
        else:
            print("Please enter a valid choice!")
    except ValueError:
        print("Please enter a valid number!")
    except ZeroDivisionError as e:
        print(f"Error : {e}")
    except Exception as e:
        print(f"An unexpected error occured : {e}")
    finally:
        print("Thank you for using the calculator. Restarting ...")