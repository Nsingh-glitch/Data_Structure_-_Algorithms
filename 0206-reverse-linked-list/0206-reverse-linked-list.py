# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def x(node):
            if node==None or node.next==None:
                return node

            new_head=x(node.next)

            temp=node.next
            temp.next=node
            node.next=None

            return new_head

        return x(head)
            

            

            
        