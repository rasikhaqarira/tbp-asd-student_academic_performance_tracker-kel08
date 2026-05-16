from typing import Optional

class MergeSortDLL:
    
 
    
    def sort(self, head: Optional[DLLNode]) -> Optional[DLLNode]:
      
        if not head or not head.next:
            return head

        mid = self._get_middle(head)
        after_mid = mid.next
        
        mid.next = None
        if after_mid:
            after_mid.prev = None

        left_sorted = self.sort(head)
        right_sorted = self.sort(after_mid)

        return self._merge(left_sorted, right_sorted)

    def _get_middle(self, head: DLLNode) -> DLLNode:
       
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, a: Optional[DLLNode], b: Optional[DLLNode]) -> Optional[DLLNode]:
       
        if not a: return b
        if not b: return a

        if a.mahasiswa.ipk >= b.mahasiswa.ipk:
            result = a
            result.next = self._merge(a.next, b)
            if result.next:
                result.next.prev = result
        else:
            result = b
            result.next = self._merge(a, b.next)
            if result.next:
                result.next.prev = result
                
        return result