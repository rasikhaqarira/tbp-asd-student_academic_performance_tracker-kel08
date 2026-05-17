from src.data_structures.merge_sort import MergeSortDLL
from src.data_structures.insertion_sort import InsertionSortDLL
import time
import random

class ModulSortingDanLaporan:

    def __init__(self, sorter_merge=None, sorter_insertion=None):
        self.merge_engine = sorter_merge if sorter_merge else MergeSortDLL()
        self.insertion_engine = sorter_insertion if sorter_insertion else InsertionSortDLL()

    def urutkan_dan_ranking(self, bst_mhs):
        mhs_list = bst_mhs.inorder()
        if not mhs_list:
            return None
            
        dll_ranking = MahasiswaDLL()
        for mhs in mhs_list:
            dll_ranking.tambah_di_akhir(mhs)
            
        dll_ranking.head = self.merge_engine.sort(dll_ranking.head)
        return dll_ranking

    def jalankan_benchmark(self, dll_mhs_class, node_class, mhs_class):
        ukuran_uji = [20, 60, 200]
        prodi_pool = ["Teknik Elektro", "Informatika", "Mesin", "Sipil", "Kimia"]

        for n in ukuran_uji:
            list_m = dll_mhs_class()
            list_i = dll_mhs_class()

            for idx in range(n):
                mhs_mock = mhs_class(
                    nim=f"21{random.randint(100000, 999999)}",
                    nama=f"Mhs-{idx}",
                    prodi=random.choice(prodi_pool),
                    angkatan=random.choice([2021, 2022, 2023]),
                    ipk=round(random.uniform(2.0, 4.0), 2)
                )
                list_m.tambah_di_akhir(mhs_mock)
                
                node_ins = node_class(mhs_mock)
                if list_i.head is None:
                    list_i.head = list_i.tail = node_ins
                else:
                    node_ins.prev = list_i.tail
                    list_i.tail.next = node_ins
                    list_i.tail = node_ins

            t0 = time.perf_counter()
            list_m.head = self.merge_engine.sort(list_m.head)
            t_merge = (time.perf_counter() - t0) * 1000

            t1 = time.perf_counter()
            list_i.head = self.insertion_engine.sort(list_i.head)
            t_insert = (time.perf_counter() - t1) * 1000

            print(f"N: {n} -> Merge: {t_merge:.4f} ms | Insertion: {t_insert:.4f} ms")

    def hitung_distribusi(self, bst_mhs):
        mhs_list = bst_mhs.inorder()
        if not mhs_list:
            return None

        prodi_sums = {}
        prodi_counts = {}
        angkatan_sums = {}
        angkatan_counts = {}

        for m in mhs_list:
            prodi_sums[m.prodi] = prodi_sums.get(m.prodi, 0.0) + m.ipk
            prodi_counts[m.prodi] = prodi_counts.get(m.prodi, 0) + 1

            angkatan_sums[m.angkatan] = angkatan_sums.get(m.angkatan, 0.0) + m.ipk
            angkatan_counts[m.angkatan] = angkatan_counts.get(m.angkatan, 0) + 1

        for prd in prodi_sums:
            avg = prodi_sums[prd] / prodi_counts[prd]
            print(f"  Program Studi {prd:<15} : {avg:.2f} (Total: {prodi_counts[prd]} mhs)")

        for ang in sorted(angkatan_sums.keys()):
            avg = angkatan_sums[ang] / angkatan_counts[ang]
            print(f"  Angkatan Tahun {ang}        : {avg:.2f} (Total: {angkatan_counts[ang]} mhs)")