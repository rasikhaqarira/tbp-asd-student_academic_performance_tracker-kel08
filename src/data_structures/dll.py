class LLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class DLLNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class TranskripNilai:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def tambah_nilai(self, nilai):
        new_node = DLLNode(nilai)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def hapus_terakhir(self):
        if not self.tail: return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return data

    def filter_semester(self, k):
        res = []
        curr = self.head
        while curr:
            if curr.data.semester == k:
                res.append(curr.data)
            curr = curr.next
        return res

    def hitung_ipk(self, grade_map):
        if self._size == 0: return 0.0
        total_points = 0.0
        total_sks = 0
        curr = self.head
        while curr:
            grade_val = grade_map.get(curr.data.grade, 0.0)
            total_points += (grade_val * curr.data.sks)
            total_sks += curr.data.sks
            curr = curr.next
        return round(total_points / total_sks, 2) if total_sks > 0 else 0.0

    def __len__(self):
        return self._size
    def _len_(self):
        return self._size
