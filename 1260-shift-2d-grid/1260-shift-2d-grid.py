class Solution:
    def shiftGrid(self, grid: List[List[int]], t: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        temp=[0 for _ in range(m*n) ]

        mult=0
        for i in range(m):
            for j in range(n):
                temp[j+mult]=grid[i][j]

            mult+=n

        t%=m*n
            
        def x(temp,k):
            n=len(temp)
            ans=[0]*n

            for i in range(n):
                ans[i]=temp[(i+k)%n]
            return ans

        new=x(temp,(m*n)-t)   

        mult=0
        for i in range(m):
            for j in range(n):
                
                grid[i][j]=new[j+mult]

            mult+=n

        return grid