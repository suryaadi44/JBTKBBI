from datetime import datetime
from rich import print
from rich.table import Table

class Stack:
    stack = []
    timestamp = []

    def addHistory(self, kata):
        self.stack.insert(0, kata)
        self.timestamp.insert(0, datetime.now().strftime("%H:%M:%S"))

        if len(self.stack) > 10:
            self.stack.pop()
            self.timestamp.pop()

    def printHistory(self):
        if (not self.checkListHistory()):
            print("Riwayat kosong")
            return 0

        print(f"Jumlah Daftar Riwayat : {len(self.stack)}")
        table = Table()
        table.add_column("No", style="cyan", no_wrap=True)
        table.add_column("Kata", style="magenta")
        table.add_column("Time", style="green")

        for i in range(len(self.stack)):
            table.add_row(str(i + 1), self.stack[i], self.timestamp[i])
        print(table)

        return 1

    def deleteHistory(self):
        if (not self.checkListHistory()):
            print("Riwayat kosong")
            return

        self.stack.clear()
        print("Daftar Riwayat terhapus")

    def checkListHistory(self):
        if(len(self.stack) == 0):
            return 0
        return 1

    def searchHistory(self, index):
        if len(self.stack) > index and index >= 0:
            return self.stack[index]
        return None
