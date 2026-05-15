import sys
import os
# Menambahkan root directory ke sys.path agar bisa import folder src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import NilaiMatkul, GRADE_MAP
from src.data_structures.bst import BSTNodeMhs 
from src.modules.modul_1 import ModulTranskrip 

def test_kalkulasi_ipk():
    print("--- Testing Modul 1: DLL & IPK Calculation ---")
    # Mock data mahasiswa (bungkus dalam node)
    class MockMhs:
        def __init__(self): self.ipk = 0.0
    
    node = BSTNodeMhs(MockMhs())
    mod1 = ModulTranskrip()
    
    # Tambah 2 nilai
    n1 = NilaiMatkul("EL101", "Matkul A", 3, "A", 1) # 4.0 * 3 = 12
    n2 = NilaiMatkul("EL102", "Matkul B", 3, "B", 1) # 3.0 * 3 = 9
    
    mod1.tambah_entri_nilai(node, n1, GRADE_MAP)
    ipk_akhir = mod1.tambah_entri_nilai(node, n2, GRADE_MAP)
    
    # (12 + 9) / 6 = 3.5
    assert ipk_akhir == 3.5
    print(f"Hasil IPK: {ipk_akhir} | Status: PASSED")

if __name__ == "__main__":
    test_kalkulasi_ipk()