## Student Academic Performance Tracker (Topik 8)
### Kelompok 8
Aplikasi berbasis CLI untuk mengelola data akademik mahasiswa menggunakan struktur data murni Python tanpa library eksternal.
### 🛠️ Struktur Data & Algoritma Utama
Sesuai dengan spesifikasi Topik 8, sistem ini mengintegrasikan:
- Binary Search Tree (BST): Penyimpanan database mahasiswa berbasis NIM (Pencarian O(logn)).
- Doubly Linked List (DLL): Penyimpanan transkrip nilai per mahasiswa (Insert/Remove Tail O(1)).
- Stack: Fitur Undo global untuk pembatalan input nilai terakhir (O(1)).
- Graph (DAG): Validasi prasyarat mata kuliah menggunakan Kahn's Algorithm (O(V+E)).
### 👥 Pembagian Tugas
Berdasarkan data kontributor GitHub:
| Nama Anggota | NIM | Kontribusi Modul |
| :--- | :--- | :--- |
| **Rasikha Qarira Rohmad** | 25051030025 | **Modul 2 & 3:** Implementasi *Binary Search Tree* (BST) untuk basis data mahasiswa (NIM) dan *Stack* untuk mekanisme *Undo* nilai. |
| **Muadi Ma’rufin** | 25051030001 | **Modul 1 & 6:** Implementasi *Doubly Linked List* (DLL) untuk transkrip nilai dan perancangan Antarmuka Utama (CLI). |
| **Eksan Satya Purnama** | 25051030024 | **Modul 4:** Implementasi *Graph* DAG untuk pemodelan prasyarat mata kuliah dan algoritma *Topological Sort*. |
| **Faiq Ridha Prasetya** | 25051030035 | **Modul 5:** Implementasi fitur *Ranking* & *Sorting* IPK menggunakan algoritma *Merge Sort* dan *Insertion Sort*. |
### 🚀 Cara Menjalankan Aplikasi
- Clone Repositori
- Masuk ke Direktori Proyek
- Jalankan Program
### ⌨️ Contoh Perintah CLI (Input/Output)
Setiap perintah akan menampilkan analisis Big-O operasinya:
- INPUT_NILAI <nim> <kode_mk> <grade>: Menambah nilai mahasiswa.
- RANKING_IPK: Mengurutkan mahasiswa berdasarkan prestasi (Merge Sort).
- PRASYARAT_CEK <nim> <kode_mk>: Memvalidasi apakah mahasiswa boleh mengambil mata kuliah tersebut.
- UNDO_NILAI <nim>: Membatalkan input nilai terakhir.
### 🧪 Menjalankan Unit Test
Proyek ini menggunakan Pytest untuk memastikan kualitas kode.
python -m pytest tests/
