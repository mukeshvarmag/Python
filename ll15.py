# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        start=A
        arr=[]
        while start:
            arr.append(start.val)
            start=start.next
        arr1=arr[B-1:C]
            
        arr[:]=arr[0:B-1]+arr1[::-1]+arr[C:len(arr)]
        start=A
        while arr:
            start.val=arr.pop(0)
            start=start.next
        return A    

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        
        # 1->2->3->4->5->NULL, m = 2 and n = 4,
        # 1->4->3->2->5->NULL.

        head = A
        current = A
        prv = None
        nxt = None
        
        step = 1
        
        while current is not None:
            
            if step < B:
                prv = current
                current = current.next

            if step >= B and step <= C:
                if step == B:
                # this is a start of the reversed list
                    last_non_reversed = prv
                    last_reversed = current
                
                if step == C:
                    # this is the end of the reversed list
                    first_reversed = current
                    first_non_reversed = current.next
                
                # part that does reverse
                nxt = current.next
                current.next = prv
                prv = current
                current = nxt

            if step > C:
                # We can skip these steps
                break
            
            step += 1
        
        if last_non_reversed is not None:
            last_non_reversed.next = first_reversed
            
        last_reversed.next = first_non_reversed
        
        if B == 1:
            # In this case we did reverse from the very first element
            head = prv
            
        return head

