from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    prodi: str
    angkatan: int
    ipk: float = 0.0
    matkul_lulus: List[str] = field(default_factory=list)

class DLLNode:
    """Node murni untuk Doubly Linked List (DLL)"""
    def __init__(self, mahasiswa: Mahasiswa):
        self.mahasiswa = mahasiswa
        self.prev: Optional[DLLNode] = None  # Menunjuk ke node sebelumnya
        self.next: Optional[DLLNode] = None  # Menunjuk ke node setelahnya

class MahasiswaDLL:
    """Database linear berbasis Doubly Linked List"""
    def __init__(self):
        self.head: Optional[DLLNode] = None
        self.tail: Optional[DLLNode] = None

    def tambah_di_akhir(self, mahasiswa: Mahasiswa):
        """Operasi Append - Kompleksitas: O(1) karena ada pointer tail"""
        new_node = DLLNode(mahasiswa)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def tampilkan_semua(self):
        """Traversal Forward - Kompleksitas: O(n)"""
        current = self.head
        if not current:
            print("Database kosong.")
            return
        while current:
            m = current.mahasiswa
            print(f"NIM: {m.nim} | Nama: {m.nama:10} | IPK: {m.ipk:.2f}")
            current = current.next