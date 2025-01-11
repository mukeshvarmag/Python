class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        start =A
        sor=[]
        while start:
            sor.append(start.val)
            start=start.next
        sor.sort()
        start=A
        while sor:
            start.val = sor.pop(0)
            start=start.next
    
        return A  