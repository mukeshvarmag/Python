# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        length = 0
        cur = A
        while cur:     ##calculating the length of the list
            length += 1
            cur = cur.next
        if B >= length:    ## if this is the case deleting the head node of the list
            return A.next
        n = length - B    ## calucalting the node to be removed from listhead (node index starts with 'zero')
        count = 0
        prev = None
        cur = A
        while count < n:
            prev = cur
            cur = cur.next
            count += 1
        if cur.next is not None:    ## cur is the node required to be removed
            prev.next = cur.next    ## removing the cur node from list by linking the prev node directly to next of the cur node
        else:
            prev.next = None
        return A 