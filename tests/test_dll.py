import sys
import os
# Menambahkan root directory ke sys.path agar bisa import folder src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.bst import BSTNodeMhs 
from src.modules.modul_1 import ModulTranskrip 

GRADE_MAP = {
    "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "D": 1.0, "E": 0.0
}

class NilaiMatkul:
    def __init__(self, kode, nama, sks, grade, semester):
        self.kode = kode          
        self.nama = nama
        self.sks = sks            
        self.grade = grade        
        self.semester = semester  

    @property
    def nilai_huruf(self):
        return self.grade

def test_kalkulasi_ipk():
    print("\n--- Testing Modul 1: DLL & IPK Calculation ---")
    
    class MockMhs:
        def __init__(self): 
            self.nim = "21006001" 
            self.ipk = 0.0
            self.transkripsi = None
    
    node = BSTNodeMhs(MockMhs())
    mod1 = ModulTranskrip()
    
    n1 = NilaiMatkul("ELT60213", "Algoritma dan Struktur Data", 3, "A", 1)  
    n2 = NilaiMatkul("INF10203", "Dasar Pemrograman", 3, "B", 1)             
    
    mod1.tambah_entri_nilai(node, n1, GRADE_MAP)
    ipk_akhir = mod1.tambah_entri_nilai(node, n2, GRADE_MAP)
    
    assert ipk_akhir == 3.5
    print(f"Hasil IPK: {ipk_akhir} | Status: PASSED")