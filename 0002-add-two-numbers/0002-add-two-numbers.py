# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def Ll(x,y):
    n=Node(x)
    y.next=n
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        curr=dummy
        t1=l1
        t2=l2
        carry=0
        while t1!=None or t2!=None:
            Sum=carry
            if t1:Sum+=t1.val
            if t2:Sum+=t2.val
            carry=Sum//10
            n=ListNode(Sum % 10)
            curr.next=n
            curr=curr.next

            if t1:t1=t1.next
            if t2:t2=t2.next
        if carry==1:
            new=ListNode(1)
            curr.next=new
        return dummy.next
            

            

        