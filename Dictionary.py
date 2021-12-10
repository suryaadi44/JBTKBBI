import os
import sys
import csv
import time
from rich import print
from lib.hash import Hash as Hash
import lib.system as system

fileNames = ['kbbi_a.csv', 'kbbi_b.csv', 'kbbi_c.csv', 'kbbi_d.csv', 'kbbi_e.csv', 'kbbi_f.csv', 'kbbi_g.csv', 'kbbi_h.csv', 'kbbi_i.csv', 'kbbi_j.csv', 'kbbi_k.csv', 'kbbi_l.csv', 'kbbi_m.csv','kbbi_n.csv', 'kbbi_o.csv', 'kbbi_p.csv', 'kbbi_q.csv', 'kbbi_r.csv', 'kbbi_s.csv', 'kbbi_t.csv', 'kbbi_u.csv', 'kbbi_v.csv', 'kbbi_w.csv', 'kbbi_x.csv', 'kbbi_y.csv', 'kbbi_z.csv']
defaultDB = "shuffled_kbbi_python.csv"

debug = 0

def loadDB(file):
    # Memecah DB menjadi beberapa file sesuai alfabet di huruf pertama dari kata
    with open(file, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            kata, arti = row[0], row[1]

            index = Hash.calcHash(kata)
            fileData = open(f'DB\{fileNames[index]}', 'a', encoding='utf-8')
            fileData.write(f'"{kata}","{arti}"\n')
            fileData.close()

            line_count += 1
        if debug:
            print(f'Processed {line_count} lines.')
            time.sleep(0.5)


def loadTable(hashTable, indeks=-1):
    # Memasukan semua kata dan arti kata dari masing masing file ke table hashnya masing masing
    # Secara default akan meload semua table, tapi jika diberikan nilai indeks, maka hanya indeks tersebut yang akan di load
    for i in range(0, 26):
        if indeks == -1 or indeks == i:
            file = f'DB/{fileNames[i]}'
            with open(file, encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    kata, arti = row[0], row[1]

                    hashTable.add(i, kata, arti)

                    line_count += 1
                if debug:
                    print(f'{fileNames[i]} : Processed {line_count} lines.')
                    time.sleep(0.5)


def commandLineMode(hash, kata):
    #Program dijalankan dengang langsung memberikan kata tanpa melewati menu
    print(hash.search(kata.lower()))

def interactiveMode(hash):
    #Program interaktif melalui menu
    while True:
        try:
            system.clear()
            print("Menu :")
            print(" 1.Search")
            print(" 2.History [blink bold red](TBA)[/blink bold red]")
            print(" 3.Settings [blink bold red](TBA)[/blink bold red]")
            print(" 4.Keluar")
            
            pil = int(input("Masukan Pilihan : "))

            if pil == 1:
                kata = input("\nMasukan Kata : ")
                hasil = hash.search(kata.lower())

                if hasil is not None :
                    print(f'Kata {kata} ditemukan')
                    print(f'\n{kata} :')
                    print(hasil)
                else:
                    print("Kata Tidak Ditemukan")
            elif pil == 4:
                break
            else:
                print("[blink bold red]Feature TBA[/blink bold red]")

        except (ValueError, IndexError):
            print(f"[blink bold red] Incorrect Input!![/blink bold red]")

        system.pause()
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
    print(data)
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
            access()


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
                        if not os.path.exists(f'DB/'):
                            os.mkdir("DB/")
                            loadDB(defaultDB)

                        hash = Hash()
                        loadTable(hash)

                        if len(sys.argv) == 1:
                            interactiveMode(hash)
                        else:
                            commandLineMode(hash, sys.argv[1])

                    else:
                        print("Password atau Username anda salah")
                except:
                    print("Terjadi kesalahan")
            else:
                print("username tidak terdaftar")
        except:
            print("Login Eror")


def home(option=None):
    option = input("Login | Signup: ")
    if option == 'Login':
        access()
    elif option == 'Signup':
        register()
    else:
        print("please, enter an option")


def main():
    home()

if __name__ == '__main__':
    main()
