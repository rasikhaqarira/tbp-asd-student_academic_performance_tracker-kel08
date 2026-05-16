import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_structures.linked_list import MahasiswaDLL
from src.data_structures.linked_list import DLLNode
from src.data_structures.merge_sort import MergeSortDLL
from src.data_structures.insertion_sort import InsertionSortDLL
from dataclasses import dataclass, field
from typing import List
import time
import random

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    prodi: str
    angkatan: int
    ipk: float = 0.0
    matkul_lulus: List[str] = field(default_factory=list)

def running_test_sort():
    ukuran_uji = [20, 60, 200]
    prodi_pool = ["Teknik Elektro", "Informatika", "Mesin", "Sipil", "Kimia"]
    
    merge_engine = MergeSortDLL()
    insertion_engine = InsertionSortDLL()

    print("\nHasil uji runtime (dalam ms):")
    print("N\tMerge\tInsertion")

    for n in ukuran_uji:
        list_m = MahasiswaDLL()
        list_i = MahasiswaDLL()

        for idx in range(n):
            mhs_mock = Mahasiswa(
                nim=f"21{random.randint(100000, 999999)}",
                nama=f"Mhs-{idx}",
                prodi=random.choice(prodi_pool),
                angkatan=random.choice([2021, 2022, 2023]),
                ipk=round(random.uniform(2.0, 4.0), 2)
            )
            list_m.tambah_di_akhir(mhs_mock)
            
            node_ins = DLLNode(mhs_mock)
            if list_i.head is None:
                list_i.head = list_i.tail = node_ins
            else:
                node_ins.prev = list_i.tail
                list_i.tail.next = node_ins
                list_i.tail = node_ins

        t0 = time.perf_counter()
        list_m.head = merge_engine.sort(list_m.head)
        t_merge = (time.perf_counter() - t0) * 1000

        t1 = time.perf_counter()
        list_i.head = insertion_engine.sort(list_i.head)
        t_insert = (time.perf_counter() - t1) * 1000

        print(f"{n}\t{t_merge:.4f}\t{t_insert:.4f}")

if __name__ == "__main__":
    running_test_sort()