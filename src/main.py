from dataclasses import dataclass 
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

# --- MODUL BINARY SEARCH TREE (BST) ---

class BSTNode:
    """Node untuk menyimpan objek Mahasiswa dalam pohon."""
    def __init__(self, mahasiswa: Mahasiswa):
        self.mahasiswa = mahasiswa
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

class MahasiswaBST:
    """Struktur data untuk pencarian Mahasiswa berdasarkan NIM."""
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, mahasiswa: Mahasiswa):
        """Menyisipkan mahasiswa baru. Efisiensi: O(log n) rata-rata."""
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
        """Mencari data mahasiswa berdasarkan NIM. Efisiensi: O(log n)."""
        return self._search_recursive(self.root, nim)

    def _search_recursive(self, node: Optional[BSTNode], nim: str) -> Optional[Mahasiswa]:
        if node is None or node.mahasiswa.nim == nim:
            return node.mahasiswa if node else None
        
        if nim < node.mahasiswa.nim:
            return self._search_recursive(node.left, nim)
        return self._search_recursive(node.right, nim)

    def tampilkan_semua(self, node: Optional[BSTNode] = None):
        """In-order Traversal untuk menampilkan mahasiswa urut berdasarkan NIM."""
        if node is None:
            node = self.root
        
        if node.left: self.tampilkan_semua(node.left)
        print(f"NIM: {node.mahasiswa.nim} | Nama: {node.mahasiswa.nama}")
        if node.right: self.tampilkan_semua(node.right)

# --- TESTING SEDERHANA ---
if __name__ == "__main__":
    bst = MahasiswaBST()
    # Dummy data
    m1 = Mahasiswa("2026002", "Andi", "Teknik Elektro", 2026)
    m2 = Mahasiswa("2026001", "Budi", "Informatika", 2026)
    
    bst.insert(m1)
    bst.insert(m2)
    
    hasil = bst.cari_nim("2026001")
    if hasil:
        print(f"Ditemukan: {hasil.nama} dari {hasil.prodi}")