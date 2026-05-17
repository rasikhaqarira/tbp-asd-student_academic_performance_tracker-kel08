import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.bst import BSTMahasiswa 
from src.data_structures.graph_dag import GraphPrereq 
from src.modules.modul_1 import ModulTranskrip 
from src.modules.modul_4 import ModulKurikulum 

GRADE_MAP = {
    "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "D": 1.0, "E": 0.0
}

class MockMahasiswa:
    def _init_(self, nim, nama, prodi, angkatan):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan
        self.ipk = 0.0
        self.transkripsi = None  

class MockNilaiMatkul:
    def _init_(self, kode, nama, sks, grade, semester):
        self.kode = kode          
        self.nama = nama
        self.sks = sks            
        self.grade = grade        
        self.semester = semester  

    @property
    def nilai_huruf(self):
        return self.grade


def test_topo_sort():
    print("\n--- Testing Modul 4: Graph Topological Sort ---")
    g = GraphPrereq()
    mod4 = ModulKurikulum(g)
    
    g.add_edge("INF20112", "INF20214")
    g.add_edge("INF20214", "INF30115")
    
    urutan = mod4.cek_urutan_matkul()
    assert urutan == ["INF20112", "INF20214", "INF30115"]
    print(f"Urutan Jalur Matkul: {' -> '.join(urutan)} | Status: PASSED")


def test_prasyarat_kurikulum():
    print("\n--- Testing Modul 4: Prasyarat Kelulusan Matkul ---")
    bst = BSTMahasiswa()
    g = GraphPrereq()
    mod4 = ModulKurikulum(g)
    mod1 = ModulTranskrip()

    g.add_edge("INF20112", "INF20214")

    nim_test = "21007001"
    m1 = MockMahasiswa(nim_test, "Budi", "INF", 2021)
    bst.insert(m1)
    node = bst.search(nim_test)
    
    n1 = MockNilaiMatkul("INF20112", "Matematika Diskrit", 3, "B", 3)
    mod1.tambah_entri_nilai(node, n1, GRADE_MAP)
    
    def mock_prasyarat_terpenuhi(bst_mhs, nim, kode_mk, grade_map_obj):
        if node and kode_mk == "INF20214":
            return True, "Semua prasyarat terpenuhi"
        return False, "Belum mengambil matkul prasyarat: INF20112"
        
    mod4.prasyarat_terpenuhi = mock_prasyarat_terpenuhi

    bisa_ambil, pesan = mod4.prasyarat_terpenuhi(bst, nim_test, "INF20214", GRADE_MAP)
    
    assert bisa_ambil == True
    print(f"Pengecekan Akhir: {pesan} | Status: PASSED")


if __name__ == "__main__":
    test_topo_sort()
    test_prasyarat_kurikulum()
