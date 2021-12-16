class Stack:
    stack = [];

    def addHistory(self, kata):
        self.stack.append(kata)

    def printHistory(self):
        if (not self.checkListHistory()):
            print("Riwayat kosong")
            return 0
        
        print(f"Daftar Riwayat : {len(self.stack)}")
        for i in range(len(self.stack)):
            print(f"{i + 1} {self.stack[i]}")
        
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
        for i in range (len(self.stack)):
            if i == index:
                return self.stack[i]
        
        return None
