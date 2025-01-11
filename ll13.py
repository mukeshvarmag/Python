# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        start=A
        arr=[]
        while start:
            arr.append(start.val)
            start=start.next
        n=len(arr)

        mid=(n+1)//2
        if n-mid-B<0:
            return -1
        else:
            return arr[n-mid-B]
            