    def removeNthLast(self,val):
        slow = self.head
        fast = self.head
        for _ in range(val):
            fast = fast.next
        if fast == None:
            return self.head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return self.head