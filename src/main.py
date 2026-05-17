# main.py

# Perbaikan Path: Menambahkan src.data_structures. di depannya
from src.data_structures.bst import BSTMahasiswa
from src.data_structures.stack_undo import Stack
from src.data_structures.graph_dag import GraphPrereq

# Mengimpor antarmuka baris perintah (CLI)
from cli.py import run_cli 

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
    
    # 1. Setup Kurikulum / Prasyarat di Graph DAG
    graph.tambah_matkul("ELT101", "Algoritma Pemrograman")
    graph.tambah_matkul("ELT201", "Struktur Data")
    graph.tambah_matkul("ELT301", "Kecerdasan Buatan")
    
    # Aturan prasyarat: ELT101 -> ELT201 -> ELT301
    graph.add_edge("ELT101", "ELT201") 
    graph.add_edge("ELT201", "ELT301") 
    
    # 2. Setup Data Mahasiswa di BST
    mhs1 = Mahasiswa("21000001", "Andi Syahputra", "Teknik Elektro", 2021)
    mhs2 = Mahasiswa("22000002", "Budi Santoso", "Teknik Elektro", 2022)
    mhs3 = Mahasiswa("23000003", "Citra Kirana", "Teknik Elektro", 2023)
    
    bst.insert(mhs1)
    bst.insert(mhs2)
    bst.insert(mhs3)
    
    print("[Sistem] Data awal (Dummy Data) berhasil dimuat!")

def main():
    print("="*50)
    print(" MEMUAT SISTEM INFORMASI AKADEMIK TERPADU ")
    print("="*50)
    
    # Inisialisasi struktur data dari nol (sesuai syarat dosen)
    db_mahasiswa = BSTMahasiswa()
    history_stack = Stack()
    kurikulum_graph = GraphPrereq()
    
    # Muat data awal
    setup_data_awal(db_mahasiswa, kurikulum_graph)
    
    # Panggil antarmuka CLI utama
    try:
        run_cli(db_mahasiswa, history_stack, kurikulum_graph)
    except Exception as e:
        print(f"\n[Error] Terjadi kesalahan pada CLI: {e}")

if __name__ == "__main__":
    main()