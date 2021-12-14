import os
import sys
from rich import print
from lib.hash import Hash as Hash
import lib.system as system
import lib.history as history
import lib.login as login
import lib.database as database

defaultDB = "shuffled_kbbi_python.csv"

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
            print(" 2.History")
            print(" 3.Settings")
            print(" 4.Keluar")
            
            pil = int(input("Masukan Pilihan : "))

            if pil == 1:
                kata = input("\nMasukan Kata : ")
                hasil = hash.search(kata.lower())
                history.addHistory(kata)

                if hasil is not None :
                    print(f'Kata {kata} ditemukan')
                    print(f'\n{kata} :')
                    print(hasil)
                else:
                    print("Kata Tidak Ditemukan")
            elif pil == 2:
                system.clear()
                history.printHistory()
            elif pil == 3:
                system.clear()
                print("Menu Setting :")
                print(" 1.Delete History")
                print(" 2.Add Kata")
                print(" 3.Delete Kata")
                print(" 4.Edit Kata")
                
                pilSetting = int(input("Masukan Pilihan : "))
                if pilSetting == 1:
                    history.deleteHistory()
                elif pilSetting == 3 :
                    kata = input("\nMasukan Kata Yang Ingin Dihapus: ")
                    # hasil = hash.delete(kata.lower())

                    # Memanggil fungsi hapus kata, return fungsi 1/0
                    # database.customizeKata(hash, kata.lower())

                    # if hasil is not None :
                    #     print(f'Kata {kata} berhasil dihapus')
                    # else:
                    #     print("Kata Tidak Ditemukan")
                elif pilSetting == 4:
                    kata=input("\nMasukan Kata Yang Ingin Diedit: ")
                    arti_baru=input('Masukkan arti baru :')

                    if database.customizeKata(hash, kata.lower(), arti_baru):
                        print("Arti kata berhasil diedit")
                    else:
                        print("Kata tidak ditemukan")
            elif pil == 4:
                break
            else:
                print("[blink bold red]Feature TBA[/blink bold red]")

        except (ValueError, IndexError):
            print(f"[blink bold red] Incorrect Input!![/blink bold red]")

        system.pause()

def main():
    if not os.path.exists(f'DB/'):
        os.mkdir("DB/")
        database.loadDB(defaultDB)
        
    hash = Hash()
    database.loadTable(hash)

    if len(sys.argv) == 1:
        login.home()
        interactiveMode(hash)
    else:
        commandLineMode(hash, sys.argv[1])
   
if __name__ == '__main__':
    main()