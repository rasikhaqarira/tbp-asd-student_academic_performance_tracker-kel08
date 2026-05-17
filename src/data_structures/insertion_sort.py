class InsertionSortDLL:
    def sort(self, head):
        if not head or not head.right:
            return head
        sorted_head = None
        curr = head
        while curr:
            nxt = curr.right
            curr.left = curr.right = None
            
            if not sorted_head or sorted_head.mhs.ipk < curr.mhs.ipk or \
               (sorted_head.mhs.ipk == curr.mhs.ipk and curr.mhs.nim <= sorted_head.mhs.nim):
                curr.right = sorted_head
                if sorted_head: sorted_head.left = curr
                sorted_head = curr
            else:
                search = sorted_head
                while search.right and (search.right.mhs.ipk > curr.mhs.ipk or \
                      (search.right.mhs.ipk == curr.mhs.ipk and search.right.mhs.nim < curr.mhs.nim)):
                    search = search.right
                
                curr.right = search.right
                if search.right: search.right.left = curr
                search.right = curr
                curr.left = search
            curr = nxt
        return sorted_head