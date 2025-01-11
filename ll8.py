
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
	    curr = A
	    head = prev = ListNode(None)
	    head.next = curr
	    while curr and curr.next:
	        if curr.val == curr.next.val:
	            while curr and curr.next and curr.val == curr.next.val:
	                curr = curr.next
	            # still one one of duplicate values left so advance
	            curr = curr.next
	            prev.next = curr
	        else:
	            prev = prev.next
	            curr = curr.next
	    return head.next