class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans=[]
        for i in intervals:
            u,v=i[0],i[1]

            if not ans:
                ans.append(i)
                continue
            t=ans[-1]
            if t[1]>=u:
                ans.pop()
                ans.append([t[0],max(v,t[1])])
            else:
                ans.append(i)
            
        return ans

        