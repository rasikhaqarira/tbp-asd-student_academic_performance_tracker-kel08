class QueueNode:
    """Node murni untuk Singly Linked List (SLL)"""
    def __init__(self, data):
        self.data = data
        self.next: Optional['QueueNode'] = None  # Hanya satu arah ke depan

class PureQueue:
    """Struktur Antrean (Queue) FIFO berbasis Singly Linked List"""
    def __init__(self):
        self.head: Optional[QueueNode] = None
        self.tail: Optional[QueueNode] = None
        self._size = 0

    def enqueue(self, data) -> None:
        """Memasukkan data ke antrean - Kompleksitas: O(1)"""
        new_node = QueueNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        """Mengeluarkan data dari antrean - Kompleksitas: O(1)"""
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return temp.data

    def is_empty(self) -> bool:
        return self._size == 0