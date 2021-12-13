
def register():
    db = open("database.txt", "r")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    confirm = input("Konfirmasi password: ")
    username1 = []
    password1 = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        username1.append(a)
        password1.append(b)
    data = dict(zip(username1, password1))

    if password != confirm:
        print("Password tidak sesuai")
        register()
    else:
        if len(password) <= 6:
            print("Password terlalu pendek")
            register()
        elif username in username1:
            print("Akun sudah terdaftar")
            register()
        else:
            db = open("database.txt", "a")
            db.write(username + "," + password + "\n")
            print('Success!')



def access():
    db = open("database.txt", "r")

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if not len(username or password) < 1:
        username1 = []
        password1 = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            username1.append(a)
            password1.append(b)
        data = dict(zip(username1, password1))
        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("Login Success")
                        print("Hai, ", username)
                    else:
                        print("Password atau Username anda salah")
                        home()
                except:
                    print("Terjadi kesalahan")
                    home()
            else:
                print("username tidak terdaftar")
                home()
        except:
            print("Login Eror")
            print("Anda belum memiliki akun, silahkan Signup terlebih dahulu ")
            home()
def home(option=None):
    option = int(input("1.Login | 2.Signup: "))
    if option == 1:
        access()
    elif option == 2:
        register()
    else:
        print("please, enter an option")