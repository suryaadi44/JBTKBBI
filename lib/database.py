from .hash import Hash
import os
import csv
import time

fileNames = ['kbbi_a.csv', 'kbbi_b.csv', 'kbbi_c.csv', 'kbbi_d.csv', 'kbbi_e.csv', 'kbbi_f.csv', 'kbbi_g.csv', 'kbbi_h.csv', 'kbbi_i.csv', 'kbbi_j.csv', 'kbbi_k.csv', 'kbbi_l.csv', 'kbbi_m.csv','kbbi_n.csv', 'kbbi_o.csv', 'kbbi_p.csv', 'kbbi_q.csv', 'kbbi_r.csv', 'kbbi_s.csv', 'kbbi_t.csv', 'kbbi_u.csv', 'kbbi_v.csv', 'kbbi_w.csv', 'kbbi_x.csv', 'kbbi_y.csv', 'kbbi_z.csv']

debug = 0

def loadDB(file):
    # Memecah DB menjadi beberapa file sesuai alfabet di huruf pertama dari kata
    with open(file, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            kata, arti = row[0], row[1]

            index = Hash.calcHash(kata)

            with open(f'DB\{fileNames[index]}', 'a', encoding='utf-8') as fileData:
                fileData.write(f'"{kata}","{arti}"\n')
            
            line_count += 1
        if debug:
            print(f'Processed {line_count} lines.')
            time.sleep(0.5)


def loadTable(hashTable, indeks=-1):
    # Memasukan semua kata dan arti kata dari masing masing file ke table hashnya masing masing
    # Secara default akan meload semua table, tapi jika diberikan nilai indeks, maka hanya indeks tersebut yang akan di load
    for i in range(0, 26):
        if indeks == -1 or indeks == i:
            file = f'/../DB/{fileNames[i]}'
            with open(os.path.dirname(__file__) + file, encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    kata, arti = row[0], row[1]

                    hashTable.add(i, kata, arti)

                    line_count += 1
                if debug:
                    print(f'{fileNames[i]} : Processed {line_count} lines.')
                    time.sleep(0.5)

def customizeKata(table, kata, arti=None):
    index = Hash.calcHash(kata)
    file = f'/../DB/{fileNames[index]}'
    file_temp = '/../DB/temp.csv'

    cek = 0 #menandai apakah proses berhasil atau tidak
    with open(os.path.dirname(__file__) + file, encoding='utf-8') as csv_file:
        with open(os.path.dirname(__file__) + file_temp, 'w', encoding='utf-8') as temp_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if row[0] == kata:
                    cek=1
                    if arti is not None:
                        temp_file.write(f'"{kata}","{arti}"\n')
                else:
                    temp_file.write(f'"{row[0]}","{row[1]}"\n')
                line_count += 1
 
    os.remove(os.path.dirname(__file__) + file)    
    os.rename(os.path.dirname(__file__) + file_temp, os.path.dirname(__file__) + file)

    # memperbarui hash table

    table.delete(index)
    loadTable(table, index)
    
    return cek