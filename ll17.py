# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        res1 = []
        res2 = []
        ans = []
        if(A is None and B is None):
            return 
        while(A):
            res1.append(A.val)
            A = A.next
        while(B):
            res2.append(B.val)
            B = B.next
        res1 = res1[::-1]
        res2 = res2[::-1]
        st1 = ""
        st2 = ""
        for i in res1:
            st1 = st1 + str(i)
        for i in res2:
            st2 += str(i)
        st1 = int(st1)
        st2 = int(st2)
        total = st1 + st2
        total = str(total)
        total = total[::-1]
        print(' -> '.join(total),end=' ')