import re
from .tree import Tree as Tree

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
        hasil = self._search(kata)
        if hasil is not None:
            arti = hasil.arti
            arti = re.sub(r'(\[*b\])([0-9])(\[*/b\])','\n \g<1>\g<2>\g<3>', arti)
            arti = re.sub(r'(\[*b\])([0-9] )', '\n\n\g<1>\g<2>', arti)
            arti = arti.replace(';;', '\n')
            arti = arti.replace('; ~', ';\n ~')
            arti = re.sub(r'\n *\n *\n', '\n\n', arti)
            arti = re.sub(r'^\n*', '', arti)
            
            return arti
        
        return None

    def _search(self, kata):
        # Panggil method di class Tree untuk search kata
        index = ord(kata[0]) - 97
        return self.table[index].search(kata)
