# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            if not head or head.next==None:return head
            else:
                new=reverse(head.next)
                temp=head.next
                head.next=None
                temp.next=head
                return new

        slow=head
        fast=head
        while  fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        first=head
        tmp=slow.next

        second=reverse(tmp)

        while second:
            if first.val!=second.val:return False
            second=second.next
            first=first.next
        
        reverse(slow.next)
        return True