import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.bst import BSTMahasiswa 
from src.modules.modul_2 import ModulDatabase 

class Mahasiswa:
    def __init__(self, nim, nama, prodi, angkatan):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan
        self.ipk = 0.0

def test_pencarian_dan_range_bst():
    print("\n--- Testing Modul 2: BST Search & Features ---")
    db = BSTMahasiswa()
    mod2 = ModulDatabase(db)
    
    m1 = Mahasiswa("21006001", "Budi", "ELT", 2021)
    m2 = Mahasiswa("21006002", "Santi", "INF", 2021)
    
    m1.ipk = 3.2
    m2.ipk = 3.8
    
    db.insert(m1)
    db.insert(m2)
    
    # 1. Tes Fitur Search NIM
    res = mod2.cari_by_nim("21006002")
    assert res.mhs.nama == "Santi"
    print(f"Cari NIM 21006002: Ditemukan ({res.mhs.nama}) | Status: PASSED")
    
    # 2. Tes Fitur Range IPK
    mhs_filter = mod2.filter_berdasarkan_rentang_ipk(3.0, 3.5)
    assert len(mhs_filter) == 1
    assert mhs_filter[0].nama == "Budi"
    print(f"Filter Range IPK (3.0 - 3.5): Ditemukan {mhs_filter[0].nama} | Status: PASSED")

if __name__ == "__main__":
    test_pencarian_dan_range_bst()