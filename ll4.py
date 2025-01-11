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
     def add_first(self,node):
         node.next=self.head
         self.head=node
     def add_last(self,node):
        if self.head is None:
            self.head=node
            node.next=None
 
     def add_after(self,target_node_data,new_node):
         if self.head is None:
             raise Exception("List is empty")
         for node in self:
             if node.data==target_node_data:
                 new_node.next=node.next
                 node.next=new_node
                 return
         raise Exception("Node with data a '%s' not found " % target_node_data )             

llst = linkedlist(["a", "b", "c", "d", "e"])


llst.add_after("d",Node("b"))

for i in llst:
    print(i)