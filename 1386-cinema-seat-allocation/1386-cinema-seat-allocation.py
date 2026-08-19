class Solution:
    def maxNumberOfFamilies(self, n: int, rS: List[List[int]]) -> int:
        ans=2*n
        hmap=dict()
        l=len(rS)
        for k in range(l):
            i,j=rS[k]
            if i not in hmap:
                hmap[i]=set()
            hmap[i].add(j)
       
        for r in hmap:
            filled=hmap[r]
            left=True
            mid=True
            right=True

            for seat in [2,3,4,5]:
                if seat in filled:
                    left=False
                    break
            
            for seat in [4,5,6,7]:
                if seat in filled:
                    mid=False
                    break
            for seat in [6,7,8,9]:
                if seat in filled:
                    right=False
                    break

            if left and right:
                groups = 2
            elif left or mid or right:
                groups = 1
            else:
                groups = 0

            ans-=2-groups

        return ans
            
            
        