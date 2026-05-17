# Main.py
import random
import numpy as np

from data_structures.bst import BSTMahasiswa, Mahasiswa
from data_structures.dll import NilaiMatkul, GRADE_MAP
from data_structures.stack_undo import Stack
from data_structures.graph_dag import GraphPrereq
from data_structures.cli import run_cli

np.random.seed(31)
random.seed(31)

PRODI = ['Teknik Elektro', 'Informatika', 'Mesin', 'Sipil', 'Kimia']
GRADES = list(GRADE_MAP.keys())

MK_LIST = [
    ('ELT101', 'Matematika Dasar', 3),
    ('ELT102', 'Fisika Dasar', 3),
    ('ELT201', 'Rangkaian Listrik', 3),
    ('ELT202', 'Elektronika', 3),
    ('ELT301', 'Sistem Digital', 3),
    ('INF101', 'Pemrograman Dasar', 3),
    ('INF201', 'Struktur Data', 3),
    ('INF301', 'Algoritma Lanjut', 3),
    ('MES101', 'Mekanika Teknik', 3),
    ('SIP101', 'Statika', 3),
]


def generate_mahasiswa(n=60):
    mhs_list = []
    for i in range(1, n + 1):
        nim = f'21{i:08d}'
        prodi = random.choice(PRODI)
        angkatan = random.choice([2021, 2022, 2023])
        mhs_list.append(Mahasiswa(nim=nim, nama=f'Mahasiswa-{i}',
                                  prodi=prodi, angkatan=angkatan))
    return mhs_list


def generate_nilai(mhs, bst):
    node = bst.search(mhs.nim)
    if not node:
        return
    for sem in range(1, 3):
        for kode, nama, sks in random.sample(MK_LIST, k=5):
            grade = random.choice(GRADES)
            node.transkripsi.tambah_nilai(
                NilaiMatkul(kode_mk=kode, nama_mk=nama, sks=sks,
                            grade=grade, semester=sem))
    bst.update_ipk(mhs.nim)


def setup_graph(graph):
    for kode, nama, _ in MK_LIST:
        graph.tambah_matkul(kode, nama)
    for prasyarat, matkul in [
        ('ELT101', 'ELT201'), ('ELT102', 'ELT201'),
        ('ELT201', 'ELT202'), ('ELT202', 'ELT301'),
        ('INF101', 'INF201'), ('INF201', 'INF301'),
        ('ELT101', 'MES101'), ('MES101', 'SIP101'),
    ]:
        graph.tambah_prasyarat(matkul, prasyarat)


def main():
    print("=" * 50)
    print("  MEMUAT SISTEM INFORMASI AKADEMIK TERPADU")
    print("=" * 50)

    bst = BSTMahasiswa()
    undo_stack = Stack()
    graph = GraphPrereq()

    setup_graph(graph)

    for mhs in generate_mahasiswa(60):
        bst.insert(mhs)
        generate_nilai(mhs, bst)

    print("[Sistem] 60 data mahasiswa berhasil dimuat!")

    run_cli(bst, undo_stack, graph)


if __name__ == '__main__':
    main()