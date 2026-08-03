# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i in range(len(lists)):
            t=lists[i]
            if t:
                heapq.heappush(heap,(t.val,i,t))

        dummy=ListNode(-1)
        curr=dummy
        while heap:
            val,ind,node=heapq.heappop(heap)
            curr.next=node
            curr=curr.next

            if node.next:
                heapq.heappush(heap,(node.next.val,ind,node.next))
        return dummy.next
