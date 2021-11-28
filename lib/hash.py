import re
from .tree import Tree as Tree

class Hash:
    def __init__(self):
        # Membuat Tree dimasing masing index Hash Table
        self._table = [Tree() for _ in range(26)]

    def add(self, index, kata, arti):
        # Panggil method di class Tree untuk insert kata dan arti
        self._table[index].insert(kata, arti)

    def search(self, kata):
        hasil = self._search(kata)
        if hasil is not None:
            arti = hasil.arti

            arti = re.sub(r'(\[*b\])([0-9])(\[*/b\])','\n \g<1>\g<2>\g<3>', arti)
            arti = re.sub(r'(\[*b\])([0-9] )', '\n\n\g<1>\g<2>', arti)
            arti = re.sub(r';;', '\n', arti)
            arti = re.sub(r'; ~', ';\n ~', arti)
            arti = re.sub(r'\n *\n *\n', '\n\n', arti)
            arti = re.sub(r'^\n*', '', arti)
            
            return arti
         
        return None

    def _search(self, kata):
        # Panggil method di class Tree untuk search kata
        index = self.calcHash(kata)
        return self._table[index].search(kata)

    @staticmethod
    def calcHash(kata):
        # Hitung index dari kata tanpa perlu menggunakan objek
        return ord(kata[0]) - 97