import os
import sys
import csv
import time
from rich import print
from lib.hash import Hash as Hash
import lib.os as system

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
            fileData = open(f'DB/{fileNames[index]}', 'a', encoding='utf-8')
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

def main():
    if not os.path.exists(f'DB/{fileNames[0]}'):
        loadDB(defaultDB)

    hash = Hash()
    loadTable(hash)

    if len(sys.argv) == 1:
        interactiveMode(hash)
    else:
        commandLineMode(hash, sys.argv[1])


if __name__ == '__main__':
    main()    
