class BSTNodeMhs:
    def __init__(self, mhs):
        self.mhs = mhs
        self.transkripsi = None
        self.left = self.right = None

class BSTMahasiswa:
    def __init__(self):
        self.root = None

    def insert(self, mhs):
        from src.data_structures.dll import TranskripNilai
        new_node = BSTNodeMhs(mhs)
        new_node.transkripsi = TranskripNilai()
        
        if not self.root:
            self.root = new_node
            return
            
        curr = self.root
        while True:
            if mhs.nim < curr.mhs.nim:
                if not curr.left:
                    curr.left = new_node
                    break
                curr = curr.left  # Pindah ke kiri
            else:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right # Pindah ke kanan

    def search(self, nim):
        curr = self.root
        while curr:
            if nim == curr.mhs.nim: return curr
            curr = curr.left if nim < curr.mhs.nim else curr.right
        return None

    def inorder(self):
        res = []
        def _traverse(node):
            if node:
                _traverse(node.left)
                res.append(node.mhs)
                _traverse(node.right)
        _traverse(self.root)
        return res
    
     # Menambah alias agar modul_2 bisa memanggil dengan nama ini
    def get_inorder_list(self):
        return self.inorder()