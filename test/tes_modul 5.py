import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.linked_list import MahasiswaDLL
from src.modules.modul_5 import ModulSortingDanLaporan
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

def test_modul_5_laporan():
    
    db = MahasiswaDLL()
    mod5 = ModulSortingDanLaporan()
    
    db.tambah_di_akhir(Mahasiswa("21001", "Andi", "Teknik Elektro", 2021, 3.0))
    db.tambah_di_akhir(Mahasiswa("21002", "Budi", "Informatika", 2022, 4.0))
    
    mod5.urutkan_dan_ranking(db)
    assert db.head.mahasiswa.ipk == 4.0
    
    mod5.hitung_distribusi(db)
    print("Status: PASSED")

if __name__ == "__main__":
    test_modul_5_laporan()