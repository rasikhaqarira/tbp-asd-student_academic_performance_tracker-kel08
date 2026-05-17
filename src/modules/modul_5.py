import time
import random

from src.data_structures.bst import BSTNodeMhs

PRODI = ["Elektro", "Informatika", "Sistem Informasi", "Teknik Komputer"]

class ModulRankingSorting:
    def __init__(self):
        pass

    def generate_mahasiswa(self, n=60): 
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
        curr = head
        
        for mhs in mhs_list[1:]:
            new_node = BSTNodeMhs(mhs)
            curr.right = new_node  # right bertindak sebagai next
            new_node.left = curr   # left bertindak sebagai prev
            curr = new_node
            
        return head

    # ================= MERGE SORT =================
    def _get_middle(self, head):
        if not head: return head
        slow, fast = head, head
        while fast.right and fast.right.right:
            slow = slow.right
            fast = fast.right.right
        return slow

    def _sorted_merge(self, a, b):
        if not a: return b
        if not b: return a

        if a.mhs.ipk >= b.mhs.ipk: # Descending (Tertinggi ke Terendah)
            result = a
            result.right = self._sorted_merge(a.right, b)
            if result.right: result.right.left = result
            result.left = None
        else:
            result = b
            result.right = self._sorted_merge(a, b.right)
            if result.right: result.right.left = result
            result.left = None
        return result

    def merge_sort(self, head):
        if not head or not head.right:
            return head
        mid = self._get_middle(head)
        next_to_mid = mid.right
        mid.right = None
        if next_to_mid: next_to_mid.left = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_mid)
        return self._sorted_merge(left, right)

    # ================= INSERTION SORT =================
    def insertion_sort(self, head):
        if not head or not head.right:
            return head
        sorted_head = None
        curr = head
        while curr:
            nxt = curr.right
            curr.left = curr.right = None
            if not sorted_head or sorted_head.mhs.ipk <= curr.mhs.ipk:
                curr.right = sorted_head
                if sorted_head: sorted_head.left = curr
                sorted_head = curr
            else:
                search = sorted_head
                while search.right and search.right.mhs.ipk > curr.mhs.ipk:
                    search = search.right
                curr.right = search.right
                if search.right: search.right.left = curr
                search.right = curr
                curr.left = search
            curr = nxt
        return sorted_head

    # ================= SIMULASI BENCHMARK & DISTRIBUSI =================
    def jalankan_simulasi_nyata(self):
        skala_n = [20, 60, 200]
        hasil = {}

        print("\n=== LAPORAN SIMULASI BENCHMARK RANKING IPK ===")
        print(f"{'N':<6} | {'Merge Sort (Riil)':<20} | {'Insertion Sort (Riil)':<20}")
        print("-" * 55)

        for n in skala_n:
            data_mentah_1 = self.generate_mahasiswa(n)
            data_mentah_2 = list(data_mentah_1)

            ll_merge = self.konversi_ke_linked_list(data_mentah_1)
            ll_insert = self.konversi_ke_linked_list(data_mentah_2)

            t0 = time.perf_counter()
            self.merge_sort(ll_merge)
            t_merge = time.perf_counter() - t0

            t0 = time.perf_counter()
            self.insertion_sort(ll_insert)
            t_insert = time.perf_counter() - t0

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
        for angk, daftar_ipk in distribusi_angkatan.items():
            print(f"   - Angkatan {angk}: Rata-rata IPK = {sum(daftar_ipk)/len(daftar_ipk):.2f}")

        print("2. Per Prodi:")
        for prod, daftar_ipk in distribusi_prodi.items():
            print(f"   - Prodi {prod:<17}: Rata-rata IPK = {sum(daftar_ipk)/len(daftar_ipk):.2f}")