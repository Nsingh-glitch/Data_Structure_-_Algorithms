class Solution:
    def shiftGrid(self, grid: List[List[int]], t: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        
        # 1. first flatten the grid and rotate it k times
        temp=[0 for _ in range(m*n) ]

          #---->better way to flatten the 2d arr into 1d 
        for i in range(m):
            for j in range(n):
                temp[n*i+j]=grid[i][j]



        t%=m*n
            
        def x(temp,k):
            n=len(temp)
            ans=[0]*n

            for i in range(n):
                ans[i]=temp[(i+k)%n]
            return ans

        # 2. after rotation now update the grid with rotate elements
        new=x(temp,(m*n)-t)   

        mult=0
        for i in range(m):
            for j in range(n):
                
                grid[i][j]=new[j+mult]

            mult+=n

        return grid