
class Node:
     def __init__(self,data):
          self.data=data
          self.next=None
    
class linkedlist:

     def __init__(self, nodes=None):
          self.head = None
          if nodes is not None:
               node = Node(data=nodes.pop(0))
               self.head = node
          for elem in nodes:
               node.next = Node(data=elem)
               node = node.next

     def __iter__(self):  
          node = self.head
          while node is not None:
             yield node.data
             node = node.next

llst = linkedlist(["a", "b", "c", "d", "e"])



for node in llst:
     print(node)

