import time
import sys
import os

# Menambahkan path src ke sys.path agar modul bisa di-import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from modules.modul_5 import ModulRankingSorting

def run_benchmark():
    # 1. PERBAIKAN: Gunakan skala data N sesuai instruksi soal
    sizes = [20, 60, 200]
    
    # Membuat satu objek solver dari modul 5 Anda
    modul_ranking = ModulRankingSorting()
    
    print("\n" + "="*70)
    print(f" {'BENCHMARK RUNTIME ALGORITMA SORTING RANKING IPK':^68}")
    print("="*70)
    print(f"{'N':<10} | {'Insertion Sort (detik)':<25} | {'Merge Sort (detik)':<25}")
    print("-" * 70)

    # Dictionary untuk menyimpan hasil waktu khusus untuk N=60
    waktu_n60 = {}

    for n in sizes:
        # 2. PERBAIKAN: Gunakan generator data asli dari modul_5 agar tipe data node sinkron (.mhs.ipk)
        data_mentah_a = modul_ranking.generate_mahasiswa(n)
        data_mentah_b = modul_ranking.generate_mahasiswa(n)

        # Konversikan list mahasiswa menjadi struktur Double Linked List (mengembalikan head node)
        head_a = modul_ranking.konversi_ke_linked_list(data_mentah_a)
        head_b = modul_ranking.konversi_ke_linked_list(data_mentah_b)

        # 3. Ukur Runtime Insertion Sort O(n^2) - kirim head node-nya
        start = time.perf_counter()
        modul_ranking.insertion_sort(head_a)
        end = time.perf_counter()
        time_insertion = end - start

        # 4. Ukur Runtime Merge Sort O(n log n) - kirim head node-nya
        start = time.perf_counter()
        modul_ranking.merge_sort(head_b)
        end = time.perf_counter()
        time_merge = end - start

        # Cetak baris data ke dalam tabel terminal
        print(f"{n:<10} | {time_insertion:<25.8f} | {time_merge:<25.8f}")
        
        # Simpan waktu khusus data N=60 untuk analisis perbandingan aktual
        if n == 60:
            waktu_n60['insertion'] = time_insertion
            waktu_n60['merge'] = time_merge
    
    print("="*70)
    
    # 3. PERBAIKAN: Menampilkan analisis perbandingan aktual langsung di terminal sebagai bukti tertulis
    if waktu_n60:
        ins_t = waktu_n60['insertion']
        mrg_t = waktu_n60['merge']
        # Mencegah pembagian dengan nol jika angka terlalu kecil
        rasio = ins_t / mrg_t if mrg_t > 0 else 0 
        
        print("\n" + "###" + " ANALISIS PERBANDINGAN AKTUAL UNTUK N = 60 " + "###")
        print(f"  * Runtime Insertion Sort : {ins_t:.8f} detik")
        print(f"  * Runtime Merge Sort     : {mrg_t:.8f} detik")
        print(f"  * Kesimpulan Aktual      : Merge Sort lebih cepat {rasio:.2f}x lipat dibanding Insertion Sort pada N=60.\n")

if __name__ == "__main__":
    run_benchmark()