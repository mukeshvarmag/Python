# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        # Assigning current pointer to start
        cur = A
        # Created empty list for storing pointers and values
        pointers = []
        values = []
        # Count variable for counting the values in the set of B values
        count = 0
        # Started traversing the list
        while(cur != None):
            # If count is less then B then append pointer to pointers and val to values
            # then increment the count and cur
            if count < B:
                pointers.append(cur)
                values.append(cur.val)
                cur = cur.next
                count += 1
            # If the set is full of B values then traverse pointers in forward order and values in reverse order
            # Replace the value of pointers with new values
            else:
                for i in range(B):
                    element = pointers.pop(0)
                    element.val = values.pop(-1)
                count = 0
        # This is to handle the last set or value after while loop end approching None pointer
        for i in range(B):
            element = pointers.pop(0)
            element.val = values.pop(-1)
        # Return the Head
        return(A)