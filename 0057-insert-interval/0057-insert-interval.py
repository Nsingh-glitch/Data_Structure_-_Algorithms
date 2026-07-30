class Solution:
    def insert(self, it: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        it.append(newInterval)
        it.sort()

        ans=[]
        for i in it:
            if not ans:
                ans.append(i)
                continue

            u,v=i[0],i[1]
            n_u,n_v=ans[-1][0],ans[-1][1]

            if u<=n_v:
                ans.pop()
                new=[n_u,max(v,n_v)]
                ans.append(new)
               
            else:
                ans.append(i)

        return ans