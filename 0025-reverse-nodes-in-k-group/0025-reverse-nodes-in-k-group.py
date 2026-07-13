# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def x(temp,k):
            k-=1
            while temp!=None and k>0:
                k-=1
                temp=temp.next
            if k>0:return None
            return temp

        def reverse(head):
            if head==None or head.next==None:
                return head
            new_node=reverse(head.next)
            front=head.next
            front.next=head
            head.next=None
            return new_node

        temp=head
        prevn=None
        while temp!=None:
            kth=x(temp,k)
            if kth==None:
                prevn.next=temp
                break
            nextn=kth.next
            kth.next=None

            reverse(temp)
            
            if temp==head:
                head=kth
                
            else:
                prevn.next=kth
            prevn=temp
            temp=nextn
        return head




            