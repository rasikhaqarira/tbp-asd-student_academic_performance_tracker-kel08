# graph_dag.py

# DIBUAT DARI NOL UNTUK MENGGANTIKAN 'deque' AGAR MEMATUHI ATURAN
class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
        
    def is_empty(self):
        return len(self.items) == 0


class GraphPrereq:
    def __init__(self):
        # Menyimpan adjacency list untuk Graph terarah (DAG)
        self.adj = {}
        self.in_degree = {}
        self.matkul = {}

    def tambah_matkul(self, kode, nama=None):
        if kode not in self.matkul:
            self.matkul[kode] = nama if nama else kode
        if kode not in self.adj:
            self.adj[kode] = []
        if kode not in self.in_degree:
            self.in_degree[kode] = 0

    def add_edge(self, u, v):
        # u adalah prasyarat dari v (Edge dari u -> v)
        self.tambah_matkul(u)
        self.tambah_matkul(v)
        
        if v not in self.adj[u]:
            self.adj[u].append(v)
            self.in_degree[v] += 1

    def topological_sort(self):
        """Mengurutkan matkul menggunakan Kahn's Algorithm dengan Queue manual"""
        init_nodes = [u for u in self.in_degree if self.in_degree[u] == 0]
        init_nodes.sort()
        
        q = Queue() # Menggunakan Queue buatan sendiri
        for node in init_nodes:
            q.enqueue(node)
            
        topo_order = []
        temp_in_degree = self.in_degree.copy()
        
        while not q.is_empty():
            u = q.dequeue()
            topo_order.append(u)
            
            for v in self.adj.get(u, []):
                temp_in_degree[v] -= 1
                if temp_in_degree[v] == 0:
                    q.enqueue(v)
                    
        # Deteksi jika terdapat siklus pada prasyarat
        if len(topo_order) != len(self.in_degree):
            return None 
            
        return topo_order

    def prasyarat_terpenuhi(self, node_mhs, kode_mk):
        """Mengecek apakah mahasiswa sudah mengambil dan lulus semua matkul prasyarat"""
        # Cari semua prasyarat (node u) yang mengarah ke matkul tujuan (node v / kode_mk)
        prasyarat_dibutuhkan = []
        for u, neighbors in self.adj.items():
            if kode_mk in neighbors:
                prasyarat_dibutuhkan.append(u)
                
        # Jika tidak ada syarat sama sekali, langsung boleh diambil
        if not prasyarat_dibutuhkan:
            return True
            
        # Ambil daftar kode matkul yang sudah lulus dari transkrip mahasiswa (Grade tidak boleh E)
        mk_lulus = []
        if node_mhs.transkripsi:
            semua_nilai = node_mhs.transkripsi.semua_nilai()
            mk_lulus = [nilai.kode_mk for nilai in semua_nilai if nilai.grade != 'E']
        
        # Cek apakah setiap prasyarat yang dibutuhkan sudah ada di daftar mk_lulus
        for mk in prasyarat_dibutuhkan:
            if mk not in mk_lulus:
                return False
        return True