import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.linked_list import MahasiswaDLL
from src.data_structures.insertion_sort import InsertionSortDLL
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

def test_insertion_sort_dll():
    print("\n--- Testing: Insertion Sort DLL ---")
    db = MahasiswaDLL()
    engine = InsertionSortDLL()
    
    db.tambah_di_akhir(Mahasiswa("21001", "Andi", "Teknik Elektro", 2021, 2.8))
    db.tambah_di_akhir(Mahasiswa("21002", "Budi", "Informatika", 2021, 3.7))
    db.tambah_di_akhir(Mahasiswa("21003", "Citra", "Mesin", 2022, 3.5))
    
    db.head = engine.sort(db.head)
    
    curr = db.head
    assert curr.mahasiswa.ipk == 3.7
    assert curr.next.mahasiswa.ipk == 3.5
    assert curr.next.next.mahasiswa.ipk == 2.8
    
    print(f"Top IPK setelah Insertion Sort: {curr.mahasiswa.ipk} | Status: PASSED")

if __name__ == "__main__":
    test_insertion_sort_dll()