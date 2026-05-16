import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.linked_list import MahasiswaDLL
from src.data_structures.linked_list import DLLNode
from dataclasses import dataclass, field
from typing import List

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    prodi: str
    angkatan: int
    ipk: float = 0.0
    matkul_lulus: List[str] = field(default_factory=list)

def test_doubly_linked_list():
    print("\n--- Testing: Doubly Linked List ---")
    db = MahasiswaDLL()
    
    m1 = Mahasiswa("21001", "Andi", "Teknik Elektro", 2021, 3.2)
    m2 = Mahasiswa("21002", "Budi", "Informatika", 2021, 3.5)
    
    db.tambah_di_akhir(m1)
    db.tambah_di_akhir(m2)
    
    assert db.head.mahasiswa.nim == "21001"
    assert db.tail.mahasiswa.nim == "21002"
    
    assert db.head.next == db.tail
    assert db.tail.prev == db.head
    
    print(f"Head NIM: {db.head.mahasiswa.nim} <-> Tail NIM: {db.tail.mahasiswa.nim} | Status: PASSED")

if __name__ == "__main__":
    test_doubly_linked_list()