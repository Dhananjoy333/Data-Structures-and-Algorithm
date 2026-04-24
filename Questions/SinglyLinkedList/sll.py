class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traversal(self):
        if self.head == None:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val,end=" ") 
                current = current.next
        print()
    def insert_at(self,val,position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current
    def delete(self,val):
        temp = self.head
        if temp.val == val :
            self.head = temp.next
            return
        else:
            found = False
            prev = None
            while temp is not None:
                if temp.val == val:
                    found = True
                    break
                prev = temp
                temp = temp.next

            if found:
                prev.next = temp.next
                return
            else:
                print("Node not found")
#Q Leetcode-876: given the head find the middle value of SLL
    # def mid(self):
    #     count = 0
    #     current = self.head
    #     midVal = self.head
    #     while current.next is not None:
    #         count += 1
    #         current = current.next
    #     if count % 2 == 0:
    #         mid = count//2
    #     else:
    #         mid = (count//2)+1
    #     while mid > 0: 
    #         mid -= 1           
    #         midVal = midVal.next            
    #     return midVal.val
#------------------optimal(slow and fast pointer/Tortoise and hare)------------------------
    # def slowAndFast(self):
    #     slowPointer = self.head
    #     fastPointer = self.head
    #     while fastPointer is not None and fastPointer.next is not None:
    #         slowPointer = slowPointer.next
    #         fastPointer = fastPointer.next.next
    #     return slowPointer.val

#Q. Reverse the linked list
    # def reverse(self):
    #     temp = self.head
    #     stack = []
    #     while temp is not None:
    #         stack.append(temp.val)
    #         temp = temp.next
    #     temp = self.head
    #     while temp is not None:
    #         lastVal = stack.pop()
    #         temp.val = lastVal
    #         temp = temp.next
#----------------------------Optimal-----------------------
    # def reverse(self):
    #     temp = self.head
    #     prev = None
    #     while temp is not None:
    #         front  = temp.next
    #         temp.next = prev
    #         prev = temp
    #         temp = front
    #     self.head = prev 

#Q.Leetcode-141: Check if given linked list is cyclic or not if yes return true else false
    # def checkCyclic(self):
    #     temp = self.head
    #     my_set = set()
    #     while temp is not None:
    #         if temp in my_set:
    #             return True
    #         my_set.add(temp)
    #         temp = temp.next
    #     return False
#---------------------------optimal(slow and fast pointer)---------------------
    # def checkCyclic(self):
    #     slow = self.head
    #     fast = self.head
    #     while fast is not None and fast.next is not None:
    #         slow = slow.next
    #         fast = fast.next.next
    #         if slow == fast:
    #             return True
    #     return False 

#Q.Leetcode-142: Find starting point of cycle in linked list
    # def startCyclic(self):
    #         temp = self.head
    #         my_set = set()
    #         while temp is not None:
    #             if temp in my_set:
    #                 return temp
    #             my_set.add(temp)
    #             temp = temp.next
    #         return None
#-------------------------optimal------------------------------
    # def startCyclic(self):
    #         slow = self.head
    #         fast = self.head
    #         while fast is not None and fast.next is not None:
    #             slow = slow.next
    #             fast = fast.next.next
    #             if slow == fast:
    #                 slow = self.head
    #                 while slow != fast:
    #                     slow = slow.next
    #                     fast = fast.next
    #                 return slow
    #         return None 

#Q. Find the length of the loop (if cycle exist show the length is no cycle length is 0)
    # def lengthCyclic(self):
    #     length = 0 
    #     temp = self.head
    #     hashMap = {}
    #     while temp is not None:
    #         if temp in hashMap:
    #             return length - hashMap[temp]
    #         hashMap[temp] = length
    #         length += 1
    #         temp = temp.next
    #     return 0
#----------------------------optimal/Floyd's cyclic detection algorithm-----------------------------------------
    # def startCyclic(self):
    #     count = 0
    #     slow = self.head
    #     fast = self.head
    #     while fast is not None and fast.next is not None:
    #         slow = slow.next
    #         fast = fast.next.next
    #         if slow == fast:
    #             count += 1
    #             slow = slow.next
    #             while slow != fast:
    #                 count += 1
    #                 slow = slow.next
    #             return count
    #     return 0
    
#Q.Leetcode-328: Return all odd indexed values in linked list to initial
    # def oddAndEven(self):
    #     temp = self.head
    #     list = []
    #     i = 0
    #     while temp is not None:
    #         list.append(temp.val)
    #         if temp.next:
    #             temp = temp.next.next
    #         else:
    #             temp = None
    #     temp = self.head.next
    #     while temp is not None:
    #         list.append(temp.val)
    #         if temp.next:
    #             temp = temp.next.next
    #         else:
    #             temp = None
    #     temp = self.head
    #     while temp is not None:
    #         temp.val = list[i]
    #         i += 1
    #         temp = temp.next 
#-----------------------optimal---------------------------
    # def oddAndEven(self):
    #     if not self.head or not self.head.next:
    #         return
    #     odd = self.head
    #     even = self.head.next
    #     evenHead = even       
    #     while even and even.next:
    #         odd.next = even.next
    #         odd = odd.next            
    #         even.next = odd.next
    #         even = even.next       
    #     odd.next = evenHead

#Q.Leetcode-19: Remove Nth node from last
    # def removeNthLast(self,val):
    #     current = self.head
    #     length = 0
    #     while current is not None:
    #         length += 1
    #         current = current.next
    #     if val > length:
    #         print("Index doesnot exist")
    #         return
    #     elif val == length:
    #         if self.head.next is not None:
    #             self.head = self.head.next
    #         else:
    #             self.head = None
    #     else:
    #         beforeRemoveIndex = (length-val)
    #         current = self.head
    #         while beforeRemoveIndex > 1:
    #             current = current.next
    #             beforeRemoveIndex -= 1
    #         current.next = current.next.next 
#-----------------------------optimal---------------------
#in single pass
    # def removeNthLast(self,val):
    #     slow = self.head
    #     fast = self.head
    #     for _ in range(val):
    #         fast = fast.next
    #     if fast == None:
    #         return self.head.next
    #     while fast.next is not None:
    #         slow = slow.next
    #         fast = fast.next
    #     slow.next = slow.next.next
    #     return self.head
              

sll = SinglyLL()
sll.append(5)
sll.append(9)
sll.append(14)
sll.append(13)
sll.append(1)
sll.append(10)
sll.append(21)
sll.append(15)
sll.append(7)
sll.traversal()
sll.removeNthLast(14)
sll.traversal()

        