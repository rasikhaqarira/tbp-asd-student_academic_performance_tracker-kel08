# tbp-asd-student_academic_performance_tracker-kel08
import numpy as np, time, random
from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple

np.random.seed(31)
random.seed(31)
PRODI = ['Teknik Elektro', 'Informatika', 'Mesin', 'Sipil', 'Kimia']

GRADE_MAP = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'D': 1.0, 'E': 0.0}

@dataclass
class Mahasiswa: 
    nim: str
    nama: str
    prodi: str
    angkatan: int
    status: int = 0.0
    ipk: float = 0.0

@dataclass
class NilaiMatkul:
    kode_mk: str
    nama_mk: str
    sks: int
    grade: str
    semester: int

class DLLNode:
""" Node Dobly Linked List. """
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class TranskripNilai:
""" Dobly Linked List menyimpan riwayat nilai per semester."""
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
