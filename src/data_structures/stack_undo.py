# stack_undo.py

# Objek untuk menyimpan riwayat input nilai yang bisa dibatalkan (undo)
class UndoRecord:
    def __init__(self, nim, kode_mk):
        self.nim = nim
        self.kode_mk = kode_mk

# Node khusus untuk Stack
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Implementasi Stack dari nol (LIFO - Last In First Out)
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    # Menambahkan data ke tumpukan paling atas
    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    # Mengambil dan menghapus data dari tumpukan paling atas
    def pop(self):
        if not self.top: 
            return None
        res = self.top.data
        self.top = self.top.next
        self._size -= 1
        return res
        
    # Hanya melihat data di tumpukan paling atas tanpa menghapusnya (Dibutuhkan oleh cli.py)
    def peek(self):
        if not self.top: 
            return None
        return self.top.data

    # Mengecek apakah tumpukan kosong
    def is_empty(self):
        return self._size == 0