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
    def __init__(self, mahasiswa: Mahasiswa): # Perbaikan typo __init__ dari kode asal
        self.mahasiswa = mahasiswa
        self.prev: Optional[DLLNode] = None
        self.next: Optional[DLLNode] = None

class MahasiswaDLL:
    """Struktur data DLL untuk menyimpan daftar mahasiswa secara linear."""
    def __init__(self): # Perbaikan typo __init__ dari kode asal
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
    def __init__(self, mahasiswa: Mahasiswa): # Perbaikan typo __init__ dari kode asal
        self.mahasiswa = mahasiswa
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

class MahasiswaBST:
    """Indexing NIM untuk pencarian cepat O(log n)."""
    def __init__(self): # Perbaikan typo __init__ dari kode asal
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
    def __init__(self): # Perbaikan typo __init__ dari kode asal
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

class GraphPrasyarat:
    """Menggunakan Directed Acyclic Graph untuk aturan pengambilan mata kuliah."""
    def __init__(self): # Perbaikan typo __init__ dari kode asal
        self.adj: Dict[str, List[str]] = {}
        self.in_degree: Dict[str, int] = {}
        self.prasyarat_list: Dict[str, List[str]] = {}

    def tambah_mk(self, kode_mk: str):
        if kode_mk not in self.adj:
            self.adj[kode_mk] = []
            self.in_degree[kode_mk] = 0
            self.prasyarat_list[kode_mk] = []

    def tambah_prasyarat(self, mk_asal: str, mk_tujuan: str):
        """Menetapkan mk_asal sebagai syarat untuk mengambil mk_tujuan."""
        self.tambah_mk(mk_asal)
        self.tambah_mk(mk_tujuan)
        self.adj[mk_asal].append(mk_tujuan)
        self.prasyarat_list[mk_tujuan].append(mk_asal)
        self.in_degree[mk_tujuan] += 1

    def dapatkan_urutan_rekomendasi(self) -> List[str]:
        """Menghasilkan urutan MK menggunakan Kahn's Algorithm (Topological Sort)."""
        temp_in_degree = self.in_degree.copy()
        queue = [mk for mk in self.adj if temp_in_degree[mk] == 0]
        urutan = []

        while queue:
            u = queue.pop(0)
            urutan.append(u)
            for v in self.adj[u]:
                temp_in_degree[v] -= 1
                if temp_in_degree[v] == 0:
                    queue.append(v)
        return urutan

    def cek_kelayakan_krs(self, mahasiswa: Mahasiswa, kode_mk_tujuan: str) -> bool:
        """Mengecek apakah mahasiswa sudah memenuhi prasyarat untuk suatu MK."""
        if kode_mk_tujuan not in self.prasyarat_list:
            print(f"[Graph] {kode_mk_tujuan} tidak memiliki prasyarat.")
            return True
            
        syarat_perlu = self.prasyarat_list[kode_mk_tujuan]
        for sp in syarat_perlu:
            if sp not in mahasiswa.matkul_lulus:
                print(f"[Graph] Ditolak: {mahasiswa.nama} belum lulus {sp} (Syarat untuk {kode_mk_tujuan}).")
                return False
        
        print(f"[Graph] Disetujui: {mahasiswa.nama} layak mengambil {kode_mk_tujuan}.")
        return True

# --- MODUL 5: RANKING & SORTING IPK (ADDITION) ---
# Sesuai instruksi Topik 8: Mengurutkan mahasiswa berdasarkan IPK menggunakan Merge Sort[cite: 595, 597].

class RankingSystem:
    def merge_sort(self, head: Optional[DLLNode]):
        """Merge Sort O(n log n) untuk mengurutkan DLL secara descending[cite: 597]."""
        if not head or not head.next:
            return head
        
        mid = self._get_middle(head)
        after_mid = mid.next
        mid.next = None
        if after_mid: after_mid.prev = None
        
        left = self.merge_sort(head)
        right = self.merge_sort(after_mid)
        
        return self._sorted_merge(left, right)

    def _get_middle(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, a, b):
        if not a: return b
        if not b: return a
        
        if a.mahasiswa.ipk >= b.mahasiswa.ipk: # Descending
            result = a
            result.next = self._sorted_merge(a.next, b)
            if result.next: result.next.prev = result
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
            if result.next: result.next.prev = result
        return result

