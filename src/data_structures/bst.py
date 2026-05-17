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
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right

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
                res.append(node)
                _traverse(node.right)
        _traverse(self.root)
        return res
    
    def get_inorder_list(self):
        return [node.mhs for node in self.inorder()]
    
    def update_ipk(self, nim, grade_map):
        """Mencari node mahasiswa dan memicu hitung ulang IPK langsung dari DLL miliknya."""
        node = self.search(nim)
        if node and node.transkripsi:
            ipk_baru = node.transkripsi.hitung_ipk(grade_map)
            node.mhs.ipk = ipk_baru
            return ipk_baru
        return 0.0

    def range_ipk(self, low, high):
        """Mengembalikan daftar objek mahasiswa yang nilai IPK-nya berada di antara rentang [low, high]."""
        res = []
        all_nodes = self.inorder() 
        
        for node in all_nodes:
            if hasattr(node.mhs, 'ipk'):
                if low <= node.mhs.ipk <= high:
                    res.append(node.mhs)
        return res