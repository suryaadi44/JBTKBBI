history = [];

def checkListHistory():
    if(len(history) == 0):
        return 0
    return 1

def addHistory(kata):
    history.append(kata)

def printHistory():
    x = checkListHistory()
    if (x == 0):
        print("Riwayat kosong")
    else:
        print("Daftar Riwayat")
        for i in range (len(history)):
            print(i + 1, end = " ")
            print(history[i])

def deleteHistory():
    x = checkListHistory()
    if (x == 0):
        print("Riwayat kosong")
    else:
        history.clear()
        print("Daftar Riwayat terhapus")