# main.py
from data_structures.bst import BSTMahasiswa
from data_structures.stack_undo import Stack
from data_structures.graph_dag import GraphPrereq
from data_structures.cli import run_cli

# --- MODEL DATA DASAR ---
class Mahasiswa:
    def __init__(self, nim, nama, prodi, angkatan):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan
        self.ipk = 0.0

def setup_data_awal(bst, graph):
    """Fungsi untuk memasukkan data awal agar program tidak kosong saat diuji dosen."""
    graph.tambah_matkul("ELT101", "Algoritma Pemrograman")
    graph.tambah_matkul("ELT201", "Struktur Data")
    graph.tambah_matkul("ELT301", "Kecerdasan Buatan")
    graph.tambah_matkul("ELT401", "Basis Data")
    graph.tambah_matkul("ELT402", "Jaringan Komputer")
    graph.tambah_matkul("ELT403", "Pemrograman Web")
    

    graph.add_edge("ELT101", "ELT201")
    graph.add_edge("ELT201", "ELT301")
    graph.add_edge("ELT201", "ELT401")
    graph.add_edge("ELT401", "ELT402")
    graph.add_edge("ELT401", "ELT403")
    
    mhs1 = Mahasiswa("21000001", "Andi Syahputra", "Teknik Elektro", 2021)
    mhs2 = Mahasiswa("22000002", "Budi Santoso", "Teknik Elektro", 2022)
    mhs3 = Mahasiswa("23000003", "Citra Kirana", "Teknik Elektro", 2023)
    mhs4 = Mahasiswa("24000004", "Dewi Lestari", "Informatika", 2024)
    mhs5 = Mahasiswa("24000005", "Rizky Ramadhan", "Sistem Informasi", 2024)
    
    bst.insert(mhs1)
    bst.insert(mhs2)
    bst.insert(mhs3)
    bst.insert(mhs4)
    bst.insert(mhs5)
    print("[Sistem] Data awal (Dummy Data) berhasil dimuat!")

def main():
    print("="*50)
    print(" MEMUAT SISTEM INFORMASI AKADEMIK TERPADU ")
    print("="*50)
    
    db_mahasiswa = BSTMahasiswa()
    history_stack = Stack()
    kurikulum_graph = GraphPrereq()
    
    setup_data_awal(db_mahasiswa, kurikulum_graph)
    
    try:
        run_cli(db_mahasiswa, history_stack, kurikulum_graph)
    except Exception as e:
        print(f"\n[Error] Terjadi kesalahan pada CLI: {e}")

if __name__ == "__main__":
    main()