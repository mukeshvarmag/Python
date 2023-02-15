# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        h=A
        
        a=0
        b=0
        
        while h:
            if h.val==0:
                a+=1
            else:
                b+=1
            h=h.next    
            
        h=A
        c=0
        while h:
            if c<a:
                c+=1
                h.val=0
            else:
                h.val=1
            h=h.next
            
        return A