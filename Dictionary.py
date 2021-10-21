import os
import csv
import platform
import re
from rich import print

fileNames = ['kbbi_a.csv', 'kbbi_b.csv', 'kbbi_c.csv', 'kbbi_d.csv', 'kbbi_e.csv', 'kbbi_f.csv', 'kbbi_g.csv', 'kbbi_h.csv', 'kbbi_i.csv', 'kbbi_j.csv', 'kbbi_k.csv', 'kbbi_l.csv', 'kbbi_m.csv','kbbi_n.csv', 'kbbi_o.csv', 'kbbi_p.csv', 'kbbi_q.csv', 'kbbi_r.csv', 'kbbi_s.csv', 'kbbi_t.csv', 'kbbi_u.csv', 'kbbi_v.csv', 'kbbi_w.csv', 'kbbi_x.csv', 'kbbi_y.csv', 'kbbi_z.csv']
defaultDB = "shuffled_kbbi_python.csv"


class Node:
    def __init__(self, kata, arti):
        self.kata = kata
        self.arti = arti
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, kata, arti):
        # Pilih mode insert tergantung root kosong atau tidak
        if self.root is None:
            self.root = Node(kata, arti)
        else:
            self._insert(kata, arti, self.root)

    def _insert(self, kata, arti, parent):
        # Tambahkan data pada tree secara rekursif
        if kata < parent.kata:
            if parent.left is None:
                parent.left = Node(kata, arti)
                return
            self._insert(kata, arti, parent.left)
        else:
            if parent.right is None:
                parent.right = Node(kata, arti)
                return
            self._insert(kata, arti, parent.right)

    def search(self, kata):
        # Cek tree jika kosong
        if self.root is not None:
            return self._search(self.root, kata)
        return None

    def _search(self, parent, kata):
        # Cari data dengan algoritma Binary Search secara rekursif
        if parent.kata == kata:
            return parent
        elif (kata > parent.kata and parent.right is not None):
            return self._search(parent.right, kata)
        elif (kata < parent.kata and parent.left is not None):
            return self._search(parent.left, kata)
        return None


class Hash:
    table = []
    
    def __init__(self):
        # Membuat Tree dimasing masing index Hash Table
        for i in range(0, 26):
            self.table.append(Tree())

    def add(self, index, kata, arti):
        # Panggil method di class Tree untuk insert kata dan arti
        self.table[index].insert(kata, arti)

    def search(self, kata):
        # Panggil method di class Tree untuk search kata
        index = ord(kata[0]) - 97
        return self.table[index].search(kata)


def loadDB(file):
    # Memecah DB menjadi beberapa file sesuai alfabet di huruf pertama dari kata
    with open(file, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            kata = row[0]
            arti = row[1]

            index = ord(kata[0]) - 97
            fileData = open(f'DB/{fileNames[index]}', 'a', encoding='utf-8')
            fileData.write(f'"{kata}","{arti}"\n')
            fileData.close()

            line_count += 1
        print(f'Processed {line_count} lines.')


def loadTable(table, indeks = -1):
    # Memasukan semua kata dan arti kata dari masing masing file ke table hashnya masing masing
    # Secara default akan meload semua table, tapi jika diberikan nilai indeks, maka hanya indeks tersebut yang akan di load
    for i in range(0, 26):
        if indeks == -1 or indeks == i:
            file = f'DB/{fileNames[i]}'
            with open(file, encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    kata = row[0]
                    arti = row[1]

                    table.add(i, kata, arti)

                    line_count += 1
                print(f'{fileNames[i]} : Processed {line_count} lines.')


def pause():
    if platform.system() == 'Windows':
        os.system('pause')
    else:
        x = input("Press Enter to continue.....")


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def main():
    if not os.path.exists(f'DB/{fileNames[0]}'):
        loadDB(defaultDB)

    table = Hash()
    loadTable(table)

    while(True):
        try:
            clear()
            print("Menu :")
            print(" 1.Search")
            print(" 2.History [blink bold red](TBA)[/blink bold red]")
            print(" 3.Settings [blink bold red](TBA)[/blink bold red]")
            pil = int(input("Masukan Pilihan : "))

            if(pil == 1):
                kata = input("\nMasukan Kata : ")
                hasil = table.search(kata.lower())
                if(hasil is not None):
                    print(f'Kata {kata} ditemukan')
                    print(f'\n{kata} :')

                    arti = hasil.arti

                    arti = re.sub(r'(\[*b\])([0-9])(\[*/b\])', '\n \g<1>\g<2>\g<3>', arti)
                    arti = re.sub(r'(\[*b\])([0-9] )', '\n\n\g<1>\g<2>', arti)
                    arti = arti.replace(';;', '\n')
                    arti = arti.replace('; ~', ';\n ~')
                    arti = re.sub(r'\n *\n *\n', '\n\n', arti)
                    arti = re.sub(r'^\n*', '', arti)

                    print(arti)
                else:
                    print("Kata Tidak Ditemukan")
            else:
                print("[blink bold red]Feature TBA[/blink bold red]")

        except (ValueError, IndexError):
                print(f"[blink bold red] Incorrect Input!![/blink bold red]")
        
        pause()


if __name__ == '__main__':
    main()
