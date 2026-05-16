class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        class Node:
            def __init__(self, d, n):
                self.data = d
                self.next = n
        
        new_node = Node(data, self.top)
        self.top = new_node
        self._size += 1

    def pop(self):
        if not self.top: return None
        res = self.top.data
        self.top = self.top.next
        self._size -= 1
        return res

    def is_empty(self):
        return self._size == 0