class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=j=0
        m=len(g)
        n=len(s)
        g.sort()
        s.sort()
        ans=0
        while i<m and j<n:
            if g[i]<=s[j]:
                ans+=1
                i+=1
                j+=1
            else:
                j+=1
        return ans
        