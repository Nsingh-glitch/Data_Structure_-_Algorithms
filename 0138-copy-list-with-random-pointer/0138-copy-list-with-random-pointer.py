"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return head
        temp=head
        new_head=Node(head.val,None,None)

        temp2=new_head
        hmap=dict()
        hmap[head]=new_head
        while temp.next!=None:
   
            new=Node(temp.next.val,None,None)
            hmap[temp.next]=new
            temp2.next=new

            temp=temp.next
            temp2=temp2.next

        temp=head
        temp2=new_head
        while temp:
            if temp.random:
                temp2.random = hmap[temp.random]

            temp = temp.next
            temp2 = temp2.next

        return new_head

                


        