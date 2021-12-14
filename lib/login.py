import lib.system as system
import csv
import os

def register():
    file_account= '/../DB/account.csv'
    with open(os.path.dirname(__file__) + file_account, 'r+') as account_file:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        confirm = input("Konfirmasi Password: ")
        username1 = []
        password1 = []

        for i in account_file:
            a, b = i.split(",")
            b = b.strip()
            username1.append(a)
            password1.append(b)
       
        if password != confirm:
            print("Password tidak sesuai")
        else:
            if len(password) <= 6:
                print("Password terlalu pendek") 
            elif username in username1:
                print("Akun sudah terdaftar")
            else:
                account_file.write(username + "," + password + "\n")
                print('Success!')
                return
        register()

def access():
    file_account= '/../DB/account.csv'
    with open(os.path.dirname(__file__) + file_account, 'r+') as account_file:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        if not len(username or password) < 1:
            username1 = []
            password1 = []
            for i in account_file:
                a, b = i.split(",")
                b = b.strip()
                username1.append(a)
                password1.append(b)
            data = dict(zip(username1, password1))
            
            try:
                if data[username]:
                    if password == data[username]:
                        print("Login Success")
                        print("Hai, ", username)
                        system.pause()
                        return
                    else:
                        print("Password atau Username anda salah") 
                else:
                    print("Username tidak terdaftar")
            except:
                print("Login Error")
                print("Anda belum memiliki akun, silahkan SignUp terlebih dahulu ")
    home()
            
def home():
    option = int(input("1.Login | 2.Sign Up: "))
    try: 
        if option == 1:
            access()
        elif option == 2:
            register()
        else:
            print("Please, enter an option")
    except ValueError:
        print("Wrong Input")
