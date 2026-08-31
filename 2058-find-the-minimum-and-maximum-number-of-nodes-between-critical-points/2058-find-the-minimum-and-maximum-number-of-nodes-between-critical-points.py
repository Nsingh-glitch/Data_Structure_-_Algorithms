# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr=head
        prev=None
        tmp=[]
        ind=1
        while curr:
            if prev!=curr and curr.next and prev:
                if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                    tmp.append(ind)
            prev=curr
            curr=curr.next
            ind+=1
        if not tmp or ind<3:
            return [-1,-1]

        maxi=max(tmp)
        mini=min(tmp)
        a=maxi-mini
        tmp.sort()
        min_diff=1e9
        for i in range(1,len(tmp)):
            min_diff=min(min_diff,tmp[i]-tmp[i-1])
        return [min_diff,a] if min_diff !=1e9 else [-1,-1]
            
