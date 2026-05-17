import time
import random

from src.data_structures.bst import BSTNodeMhs
from src.data_structures.merge_sort import MergeSortDLL
from src.data_structures.insertion_sort import InsertionSortDLL

PRODI = ["Elektro", "Informatika", "Sistem Informasi", "Teknik Komputer"]

class ModulRankingSorting:
    def __init__(self):
        self.merge_engine = MergeSortDLL()
        self.insertion_engine = InsertionSortDLL()

    def generate_mahasiswa(self, n=60): 
        random.seed(31)
        
        class Mahasiswa:
            def __init__(self, nim, nama, prodi, angkatan):
                self.nim = nim
                self.nama = nama
                self.prodi = prodi
                self.angkatan = angkatan
                self.ipk = round(random.uniform(2.0, 4.0), 2)

        mhs_list = [] 
        for i in range(1, n+1): 
            nim = f'21{i:08d}' 
            prodi = random.choice(PRODI) 
            angkatan = random.choice([2021, 2022, 2023]) 
            mhs_list.append(Mahasiswa(nim, f'Mahasiswa-{i}', prodi, angkatan)) 
        return mhs_list

    def konversi_ke_linked_list(self, mhs_list):
        if not mhs_list:
            return None
        
        head = BSTNodeMhs(mhs_list[0])
        head.left = None
        curr = head
        
        for mhs in mhs_list[1:]:
            new_node = BSTNodeMhs(mhs)
            curr.right = new_node
            new_node.left = curr
            curr = new_node
            
        curr.right = None
        return head

    def merge_sort(self, head):
        return self.merge_engine.sort(head)

    def insertion_sort(self, head):
        return self.insertion_engine.sort(head)

    # ================= SIMULASI & DISTRIBUSI =================
    def jalankan_simulasi_nyata(self):
        skala_n = [20, 60, 200]
        hasil = {}

        print("\n=== LAPORAN SIMULASI BENCHMARK RANKING IPK ===")
        print(f"{'N':<6} | {'Merge Sort (Riil)':<20} | {'Insertion Sort (Riil)':<20}")
        print("-" * 55)

        for n in skala_n:
            data_mentah_1 = self.generate_mahasiswa(n)
            data_mentah_2 = self.generate_mahasiswa(n)

            ll_merge = self.konversi_ke_linked_list(data_mentah_1)
            ll_insert = self.konversi_ke_linked_list(data_mentah_2)

            t0 = time.perf_counter()
            self.merge_sort(ll_merge)
            t_merge = time.perf_counter() - t0

            t1 = time.perf_counter()
            self.insertion_sort(ll_insert)
            t_insert = time.perf_counter() - t1

            hasil[n] = {"merge": t_merge, "insertion": t_insert}
            print(f"{n:<6} | {t_merge:.7f} detik | {t_insert:.7f} detik")
            
        self.hitung_distribusi(data_mentah_1)
            
        return hasil

    def hitung_distribusi(self, list_mahasiswa):
        distribusi_angkatan = {}
        distribusi_prodi = {}

        for mhs in list_mahasiswa:
            distribusi_angkatan[mhs.angkatan] = distribusi_angkatan.get(mhs.angkatan, []) + [mhs.ipk]
            distribusi_prodi[mhs.prodi] = distribusi_prodi.get(mhs.prodi, []) + [mhs.ipk]

        print("\n=== DATA DISTRIBUSI IPK MAHASISWA ===")
        print("1. Per Angkatan:")
        for angk in sorted(distribusi_angkatan.keys()):
            daftar_ipk = distribusi_angkatan[angk]
            print(f"    - Angkatan {angk}: Rata-rata IPK = {sum(daftar_ipk)/len(daftar_ipk):.2f}")

        print("2. Per Prodi:")
        for prod in sorted(distribusi_prodi.keys()):
            daftar_ipk = distribusi_prodi[prod]
            print(f"    - Prodi {prod:<17}: Rata-rata IPK = {sum(daftar_ipk)/len(daftar_ipk):.2f}")