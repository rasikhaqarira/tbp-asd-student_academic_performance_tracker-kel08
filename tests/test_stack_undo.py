import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import Mahasiswa, NilaiMatkul, GRADE_MAP
from src.data_structures.bst import BSTMahasiswa 
from src.data_structures.stack_undo import Stack 
from src.modules.modul_1 import ModulTranskrip # Butuh mod1 untuk isi data 
from src.modules.modul_3 import ModulUndo 

def test_undo_system():
    print("\n--- Testing Modul 3: Stack Undo ---")
    bst = BSTMahasiswa()
    stack = Stack()
    mod3 = ModulUndo(stack)
    
    m1 = Mahasiswa("2199", "Agus", "Sipil", 2021)
    bst.insert(m1)
    node = bst.search("2199")
    
    # Input nilai lalu catat di stack
    node.transkripsi.tambah_nilai(NilaiMatkul("MK1", "A", 3, "A", 1))
    mod3.catat_log("2199")
    
    assert len(node.transkripsi) == 1
    
    # Jalankan Undo
    success, nim = mod3.batalkan_aksi(bst, GRADE_MAP)
    assert success == True
    assert len(node.transkripsi) == 0
    print(f"Undo NIM {nim}: Berhasil (DLL Kosong Kembali) | Status: PASSED")

if __name__ == "__main__":
    test_undo_system()