# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:return head
        slow=head
        fast=head
        cnt=0
        curr=head
        while curr!=None:
            cnt+=1
            curr=curr.next
        k%=cnt
        if not k :return head
        while k:
            fast=fast.next
            k-=1
        
        while fast.next!=None:
            fast=fast.next
            slow=slow.next
        tmp=slow.next
        slow.next=None
        fast.next=head

        return tmp