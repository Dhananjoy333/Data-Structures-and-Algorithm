class Node:
    def __init__(self,val):
        self.prev = None
        self.val = val
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
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
    
    def insert_at(self,val,position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if current.next is None:
            print("Position out of bound")
            return
        new_node.next = current.next
        new_node.prev = current
        if current:
            current.next.prev = new_node
        current.next = new_node
    
    def traversal(self):
        current = self.head
        if self.head is None:
            print("No nodes in Linked List")
            return
        while current is not None:
            print(current.val, end=" ")
            current = current.next
        print()
    
    def delete_head(self):
        if self.head is None:
            print("No nodes in Linked List")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None
    
    def delete_last(self):
        if self.head is None:
            print("No nodes in Linked List")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.prev.next = None
    
    def delete_at(self, position):
        if self.head is None:
            print("No nodes in Linked List")
            return
        if position == 0:
            self.delete_head()
            return
        count = 0
        current = self.head
        while current and count < position - 1:
            current = current.next
            count += 1
        # position too large
        if current is None or current.next is None:
            print("Position out of bound")
            return
        # normal deletion
        temp = current.next
        current.next = temp.next
        if temp.next:
            temp.next.prev = current


dll = DoublyLL()
dll.append(5)
dll.append(13)
dll.append(12)
dll.append(11)
dll.append(14)
dll.traversal()
dll.insert_at(55,2)
dll.traversal()
dll.delete_at(6)
dll.traversal()