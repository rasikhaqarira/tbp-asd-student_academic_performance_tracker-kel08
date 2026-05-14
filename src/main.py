from dataclasses import dataclass 
from typing import Optional, List, Dict, Tuple 
import numpy as np
import time
import random

np.random.seed(31) 
random.seed(31) 

PRODI = ['Teknik Elektro', 'Informatika', 'Mesin', 'Sipil', 'Kimia'] 
GRADE_MAP = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 
             'C+': 2.3, 'C': 2.0, 'D': 1.0, 'E': 0.0}

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    prodi: str
    angkatan: int
    status: int = 0
    ipk: float = 0.0
    
    def __post_init__(self):
        self.transkrip = TranskripNilai()

@dataclass
class NilaiMatkul:
    kode_mk: str
    nama_mk: str
    sks: int
    grade: str
    semester: int

# --- MODUL DOUBLY LINKED LIST (DLL) ---
class DLLNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class TranskripNilai:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def tambah_nilai(self, nilai):
        """Sisip di tail. Big-O: O(1)"""
        new_node = DLLNode(nilai)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def hapus_terakhir(self):
        """Hapus dari tail (undo). Big-O: O(1)"""
        if self.head is None:
            return None
        removed_data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return removed_data

    def hitung_ipk(self):
        """Traversal untuk hitung rata-rata. Big-O: O(n)"""
        if self.head is None:
            return 0.0
        total_bobot = 0
        total_sks = 0
        current = self.head
        while current:
            grade_val = GRADE_MAP.get(current.data.grade, 0)
            total_bobot += (grade_val * current.data.sks)
            total_sks += current.data.sks
            current = current.next
        return total_bobot / total_sks if total_sks > 0 else 0.0