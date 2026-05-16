import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.linked_list import MahasiswaDLL
from src.data_structures.merge_sort import MergeSortDLL
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

def test_merge_sort_dll():
    
    db = MahasiswaDLL()
    engine = MergeSortDLL()
    
    db.tambah_di_akhir(Mahasiswa("21001", "Andi", "Teknik Elektro", 2021, 3.1))
    db.tambah_di_akhir(Mahasiswa("21002", "Budi", "Informatika", 2021, 3.9))
    db.tambah_di_akhir(Mahasiswa("21003", "Citra", "Mesin", 2022, 3.4))
    
    db.head = engine.sort(db.head)
    
    curr = db.head
    assert curr.mahasiswa.ipk == 3.9
    assert curr.next.mahasiswa.ipk == 3.4
    assert curr.next.next.mahasiswa.ipk == 3.1
    
    print(f"Top IPK setelah Merge Sort: {curr.mahasiswa.ipk} | Status: PASSED")

if __name__ == "__main__":
    test_merge_sort_dll()