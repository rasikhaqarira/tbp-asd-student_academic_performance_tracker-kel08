import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modules.modul_5 import ModulRankingSorting

def test_ranking_dan_analisis_ipk():
    print("\n--- Testing Modul 5: Ranking & Sorting IPK ---")
    mod5 = ModulRankingSorting()

    # 1. Tes apakah fungsi generator bekerja menghasilkan N=60 data
    mhs_list = mod5.generate_mahasiswa(60)
    assert len(mhs_list) == 60, "Jumlah mahasiswa hasil generate harus 60"
    assert mhs_list[0].nim.startswith("21"), "NIM harus berformat angkatan 21"
    print("Fungsi generate_mahasiswa(n=60) Dosen | Status: PASSED 🟢")

    # 2. Tes konversi list biasa ke Doubly Linked List (Memakai Node BST)
    head_ll = mod5.konversi_ke_linked_list(mhs_list)
    assert head_ll is not None, "Linked list gagal terbentuk (head kosong)"
    # Perbaikan 3: Validasi struktur datanya, bukan menebak isi namanya secara spekulatif
    assert head_ll.left is None, "Pointer left milik head harus None"
    print("Konversi Struktur ke Linked List Mandiri | Status: PASSED 🟢")

    # 3. Jalankan Simulasi Benchmark Waktu Riil N = 20, 60, 200
    analisis_waktu = mod5.jalankan_simulasi_nyata()
    assert 60 in analisis_waktu, "Skala N=60 harus ada dalam hasil analisis"
    print("Analisis Komparasi Run-Time Laporan Laprak | Status: PASSED 🟢")

if __name__ == "__main__":
    test_ranking_dan_analisis_ipk()