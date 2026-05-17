from collections import deque

class GraphPrereq:
    def __init__(self):
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
        self.tambah_matkul(u)
        self.tambah_matkul(v)
        
        if v not in self.adj[u]:
            self.adj[u].append(v)
            self.in_degree[v] += 1

    def topological_sort(self):
        init_nodes = [u for u in self.in_degree if self.in_degree[u] == 0]
        init_nodes.sort()
        
        queue = deque(init_nodes)
        topo_order = []
        temp_in_degree = self.in_degree.copy()
        
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            
            for v in self.adj.get(u, []):
                temp_in_degree[v] -= 1
                if temp_in_degree[v] == 0:
                    queue.append(v)
                    
        return topo_order
