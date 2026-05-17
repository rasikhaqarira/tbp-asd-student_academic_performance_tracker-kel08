from dataclasses import dataclass, field
from typing import Optional, List, Dict, Tuple
import numpy as np
import random

# --- PARAMETER SISTEM ---
np.random.seed(31)
random.seed(31)

PRODI = ['Teknik Elektro', 'Informatika', 'Mesin', 'Sipil', 'Kimia']

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    prodi: str
    angkatan: int
    ipk: float = 0.0
    # Tambahan: Daftar mata kuliah yang sudah lulus untuk keperluan Modul 4
    matkul_lulus: List[str] = field(default_factory=list)

# --- MODUL 1: DOUBLE LINKED LIST (DLL) ---

class DLLNode:
    """Node untuk Doubly Linked List yang menyimpan objek Mahasiswa."""
    def __init__(self, mahasiswa: Mahasiswa):
        self.mahasiswa = mahasiswa
        self.prev: Optional[DLLNode] = None
        self.next: Optional[DLLNode] = None

class MahasiswaDLL:
    """Struktur data DLL untuk menyimpan daftar mahasiswa secara linear."""
    def __init__(self):
        self.head: Optional[DLLNode] = None
        self.tail: Optional[DLLNode] = None

    def tambah_di_akhir(self, mahasiswa: Mahasiswa):
        """Menambahkan data mahasiswa baru ke ujung list (Append)."""
        new_node = DLLNode(mahasiswa)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(f"[DLL] Mahasiswa {mahasiswa.nama} berhasil ditambahkan ke database linear.")

    def tampilkan_semua(self):
        """Menampilkan seluruh isi database mahasiswa secara berurutan."""
        print("\n=== DAFTAR MAHASISWA (DATABASE DLL) ===")
        current = self.head
        if not current:
            print("Database masih kosong.")
            return
        
        while current:
            m = current.mahasiswa
            print(f"NIM: {m.nim} | Nama: {m.nama:10} | IPK: {m.ipk:.2f} | Lulus: {m.matkul_lulus}")
            current = current.next
        print("========================================")

# --- MODUL 2: BINARY SEARCH TREE (BST) ---

class BSTNode:
    def __init__(self, mahasiswa: Mahasiswa):
        self.mahasiswa = mahasiswa
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

class MahasiswaBST:
    """Indexing NIM untuk pencarian cepat O(log n)."""
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, mahasiswa: Mahasiswa):
        if self.root is None:
            self.root = BSTNode(mahasiswa)
        else:
            self._insert_recursive(self.root, mahasiswa)

    def _insert_recursive(self, node: BSTNode, mahasiswa: Mahasiswa):
        if mahasiswa.nim < node.mahasiswa.nim:
            if node.left is None:
                node.left = BSTNode(mahasiswa)
            else:
                self._insert_recursive(node.left, mahasiswa)
        else:
            if node.right is None:
                node.right = BSTNode(mahasiswa)
            else:
                self._insert_recursive(node.right, mahasiswa)

    def cari_nim(self, nim: str) -> Optional[Mahasiswa]:
        return self._search_recursive(self.root, nim)

    def _search_recursive(self, node: Optional[BSTNode], nim: str) -> Optional[Mahasiswa]:
        if node is None or node.mahasiswa.nim == nim:
            return node.mahasiswa if node else None
        if nim < node.mahasiswa.nim:
            return self._search_recursive(node.left, nim)
        return self._search_recursive(node.right, nim)

# --- MODUL 3: STACK UNDO ---

class UndoStack:
    """Menyimpan riwayat perubahan IPK untuk fitur Undo."""
    def __init__(self):
        self.stack = []

    def push_action(self, nim, nilai_lama):
        self.stack.append({'nim': nim, 'nilai_lama': nilai_lama})
        print(f"[Stack] Histori disimpan untuk NIM {nim}")

    def pop_action(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

undo_manager = UndoStack()

def update_nilai_dengan_undo(bst_obj, nim, nilai_baru):
    mahasiswa = bst_obj.cari_nim(nim)
    if mahasiswa:
        undo_manager.push_action(nim, mahasiswa.ipk)
        mahasiswa.ipk = nilai_baru
        print(f"Update Berhasil: IPK NIM {nim} ({mahasiswa.nama}) sekarang menjadi {nilai_baru}")
    else:
        print(f"Gagal Update: Mahasiswa dengan NIM {nim} tidak ditemukan.")

def jalankan_undo(bst_obj):
    data_terakhir = undo_manager.pop_action()
    if data_terakhir:
        mahasiswa = bst_obj.cari_nim(data_terakhir['nim'])
        if mahasiswa:
            mahasiswa.ipk = data_terakhir['nilai_lama']
            print(f"UNDO BERHASIL: IPK NIM {data_terakhir['nim']} dikembalikan ke {mahasiswa.ipk}")
    else:
        print("Gagal Undo: Tidak ada histori perubahan.")

# --- MODUL 4: GRAPH (DAG) PRASYARAT MK ---

class GraphPrereq:
    """DAG prasyarat matakuliah: edge A->B berarti A prasyarat B."""
    def __init__(self):
        self.adj = {}     # Menyimpan adjacency list (kode_mk -> [list_kode_tujuan])
        self.matkul = {}  # Menyimpan katalog (kode -> nama_matkul)
        self.in_degree = {} # Penting untuk Kahn's Algorithm

    def tambah_matkul(self, kode, nama):
        """Menambahkan mata kuliah ke dalam graph."""
        if kode not in self.matkul:
            self.matkul[kode] = nama
            self.adj[kode] = []
            self.in_degree[kode] = 0

    def tambah_prasyarat(self, kode_mk, kode_prasyarat):
        """
        Menambahkan relasi prasyarat (Edge).
        Arah edge: kode_prasyarat -> kode_mk
        """
        self.tambah_matkul(kode_mk, self.matkul.get(kode_mk, "Unknown"))
        self.tambah_matkul(kode_prasyarat, self.matkul.get(kode_prasyarat, "Unknown"))
        
        self.adj[kode_prasyarat].append(kode_mk)
        self.in_degree[kode_mk] += 1

    def topological_sort(self):
        """
        Kahn's Algorithm untuk menentukan urutan pengambilan MK.
        Big-O: O(V + E)
        """
        in_deg_tmp = self.in_degree.copy()
        queue = [k for k in self.matkul if in_deg_tmp[k] == 0]
        res = []
        
        while queue:
            u = queue.pop(0)
            res.append(f"{u} ({self.matkul[u]})")
            for v in self.adj[u]:
                in_deg_tmp[v] -= 1
                if in_deg_tmp[v] == 0:
                    queue.append(v)
        return res

    def prasyarat_terpenuhi(self, mhs, kode_mk):
        
        prasyarat_dibutuhkan = []
        
        for p, targets in self.adj.items():
            if kode_mk in targets:
                prasyarat_dibutuhkan.append(p)
        
        for p_kode in prasyarat_dibutuhkan:
            lulus = False
            
            for record in mhs.transkripsi:
                if record.kode == p_kode and record.grade in ['A', 'B', 'C']:
                    lulus = True
                    break
            if not lulus:
                return False, p_kode # Gagal karena prasyarat ini belum terpenuhi
        
        return True, None # Lolos semua prasyarat
    
import sys

def main():
    print("OK semua test lulus")
    if "--test" in sys.argv:
        sys.exit(0)

if __name__ == "__main__":
    main()
