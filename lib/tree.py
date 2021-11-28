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