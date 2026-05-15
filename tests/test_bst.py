import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import Mahasiswa
from src.data_structures.bst import BSTMahasiswa 
from src.modules.modul_2 import ModulDatabase 

def test_pencarian_nim():
    print("\n--- Testing Modul 2: BST Search ---")
    db = BSTMahasiswa()
    mod2 = ModulDatabase(db)
    
    m1 = Mahasiswa("210001", "Budi", "Elektro", 2021)
    m2 = Mahasiswa("210002", "Santi", "Informatika", 2021)
    
    db.insert(m1)
    db.insert(m2)
    
    res = mod2.cari_by_nim("210002")
    assert res.mhs.nama == "Santi"
    print(f"Cari NIM 210002: Ditemukan ({res.mhs.nama}) | Status: PASSED")

if __name__ == "__main__":
    test_pencarian_nim()