# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def insertionSortList(A):
    arr=[]
    start=A
    while start:
        arr.append(start.val)
        start=start.next
    arr.sort()
    start=A
    while arr:
        start.val=arr.pop(0)
        start=start.next
    return A    

def insert(pos,a):
    a.next=pos.next
    pos.next=a
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head=ListNode(-2*31)
        while A:
            prev=head
            node=head.next
            while node:
                if node.val>=A.val:
                    break
                prev=node
                node=node.next
            insert(prev,ListNode(A.val))
            A=A.next
        return head.next