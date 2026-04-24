class Node:
    def __init__(self,val):
        self.prev = None
        self.val = val
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None    
    def append(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def traversal(self):
        current = self.head
        if self.head is None:
            print("No nodes in Linked List")
            return
        while current is not None:
            print(current.val, end=" ")
            current = current.next
        print()

#Q. Reverse the doubly linked list
    # def reverse(self):
    #     temp = self.head
    #     if self.head is None:
    #         return self.head
    #     else:
    #         back = None
    #         while temp is not None:
    #             front = temp.next
    #             temp.next = back
    #             temp.prev = front
    #             back = temp
    #             temp = front
    #         self.head = back

#Q. Delete all occurences of a val
    # def deleteOccurences(self,val):
    #     current = self.head
    #     if current.val == None :
    #         return None
    #     if current.val == val and current.next == None:
    #         self.head = None
    #         return self.head
    #     elif current.val != val and current.next == None:
    #         return self.head
    #     if current.val == val:
    #         while current.next is not None and current.val == val:
    #             current = current.next
    #         self.head = current
    #     if self.head.val == val and self.head.next == None:
    #         return None
    #     if current.val != val:
    #         while current.next is not None:
    #             if current.val == val:
    #                 current.prev.next = current.next
    #                 current.next.prev = current.prev
    #             current = current.next
    #         if current.val == val:
    #             current.prev.next = None
    #     return self.head 
    # def deleteOccurences(self, val):
    #     if self.head is None:
    #         return None
    #     current = self.head
    #     while current is not None:
    #         if current.val == val:
    #             # If node is head
    #             if current.prev is None:
    #                 self.head = current.next
    #                 if self.head is not None:
    #                     self.head.prev = None
    #             else:
    #                 current.prev.next = current.next
    #                 if current.next is not None:
    #                     current.next.prev = current.prev
    #         current = current.next
    #     return self.head
    
   


dll = DoublyLL()
dll.append(11)
dll.append(11)
dll.append(5)
dll.append(13)
dll.append(11)
dll.append(12)
dll.append(11)
dll.append(11)
dll.append(11)
dll.append(11)
dll.append(14)
dll.append(11)
# dll.traversal()
print(dll.deleteOccurences(11))
dll.traversal()

