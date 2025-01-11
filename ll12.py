# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        if  A is None:
            return A
        even = []
        head = A
        head = head.next
        while head and head.next and head.next.next:
            even.append(head.val)
            head = head.next.next
        if head:
            even.append(head.val)
        head = A
        head = head.next
        while head and head.next and head.next.next:
            head.val = even.pop()
            head = head.next.next   
        if head and even:
            head.val = even.pop()
        return A