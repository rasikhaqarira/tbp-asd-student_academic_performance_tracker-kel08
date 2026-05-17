class MergeSortDLL:
    def _get_middle(self, head):
        if not head: return head
        slow, fast = head, head
        while fast.right and fast.right.right:
            slow = slow.right
            fast = fast.right.right
        return slow

    def _sorted_merge(self, a, b):
        if not a: return b
        if not b: return a

        pilih_a = False
        if a.mhs.ipk > b.mhs.ipk:
            pilih_a = True
        elif a.mhs.ipk == b.mhs.ipk:
            if a.mhs.nim <= b.mhs.nim:
                pilih_a = True

        if pilih_a:
            result = a
            result.right = self._sorted_merge(a.right, b)
            if result.right: result.right.left = result
            result.left = None
        else:
            result = b
            result.right = self._sorted_merge(a, b.right)
            if result.right: result.right.left = result
            result.left = None
        return result

    def sort(self, head):
        if not head or not head.right:
            return head
        mid = self._get_middle(head)
        next_to_mid = mid.right
        mid.right = None
        if next_to_mid: next_to_mid.left = None

        left = self.sort(head)
        right = self.sort(next_to_mid)
        return self._sorted_merge(left, right)