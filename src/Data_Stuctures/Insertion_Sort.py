from typing import Optional

class InsertionSortDLL:
    

    def sort(self, head: Optional[DLLNode]) -> Optional[DLLNode]:
      
        if not head or not head.next:
            return head

        sorted_head = None
        current = head

        while current:
            next_node = current.next
            
            current.prev = None
            current.next = None
            
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node

        return sorted_head

    def _sorted_insert(self, sorted_head: Optional[DLLNode], new_node: DLLNode) -> DLLNode:
        
        if not sorted_head:
            return new_node

        if new_node.mahasiswa.ipk >= sorted_head.mahasiswa.ipk:
            new_node.next = sorted_head
            sorted_head.prev = new_node
            return new_node

        current = sorted_head
        while current.next and current.next.mahasiswa.ipk > new_node.mahasiswa.ipk:
            current = current.next

        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
            
        current.next = new_node
        new_node.prev = current

        return sorted_head