# bst.py

# Node untuk Binary Search Tree (Menyimpan data Mahasiswa)
class BSTNodeMhs:
    def __init__(self, mhs):
        self.mhs = mhs
        self.transkripsi = None # Akan diisi objek Doubly Linked List (TranskripNilai)
        self.left = None
        self.right = None

# Implementasi BST dari Nol
class BSTMahasiswa:
    def __init__(self):
        self.root = None

    def insert(self, mhs):
        # Import dilakukan di sini untuk mencegah circular import
        from dll import TranskripNilai 
        new_node = BSTNodeMhs(mhs)
        new_node.transkripsi = TranskripNilai() # Setiap mahasiswa baru otomatis punya transkrip kosong
        
        if not self.root:
            self.root = new_node
            return
            
        curr = self.root
        while True:
            # Pencabangan BST: lebih kecil ke kiri, lebih besar ke kanan
            if mhs.nim < curr.mhs.nim:
                if not curr.left:
                    curr.left = new_node
                    break
                curr = curr.left
            elif mhs.nim > curr.mhs.nim:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right
            else:
                # Jika NIM sudah ada, abaikan (tidak boleh duplikat)
                break

    def search(self, nim):
        curr = self.root
        while curr:
            if nim == curr.mhs.nim: 
                return curr
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
        # Fungsi ini yang dipakai cli.py untuk mengambil array data mahasiswa sebelum di-Merge Sort
        return [node.mhs for node in self.inorder()]
    
    def update_ipk(self, nim):
        """Mencari node mahasiswa dan memicu hitung ulang IPK langsung dari DLL miliknya."""
        from dll import GRADE_MAP
        node = self.search(nim)
        if node and node.transkripsi:
            ipk_baru = node.transkripsi.hitung_ipk(GRADE_MAP)
            node.mhs.ipk = ipk_baru
            return ipk_baru
        return 0.0

    def range_ipk(self, low, high):
        """Mengembalikan daftar objek mahasiswa yang nilai IPK-nya berada di rentang [low, high]."""
        res = []
        all_nodes = self.inorder() 
        
        for node in all_nodes:
            if hasattr(node.mhs, 'ipk'):
                if low <= node.mhs.ipk <= high:
                    res.append(node.mhs)
        return res