# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr=head
        prev=None
        ind=1
        first_c_point=-1
        prev_c_point=-1
        min_dist=1e9

        while curr.next:
            if prev!=curr and prev:
                if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                    if first_c_point==-1:
                        first_c_point=ind
                        
                    else:
                        min_dist=min(min_dist,ind-prev_c_point)
                    prev_c_point=ind
            prev=curr
            curr=curr.next
            ind+=1

        if min_dist==1e9:return [-1,-1]

        return [min_dist,prev_c_point-first_c_point]
