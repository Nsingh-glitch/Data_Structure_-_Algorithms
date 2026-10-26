class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        def dfs(x,y):
            if x<0 or x>=m or y<0 or y>=n or grid[x][y]==0:
                return 0
                
            val=grid[x][y]
            grid[x][y]=0

            l=dfs(x-1,y)
            r=dfs(x+1,y)
            u=dfs(x,y+1)
            d=dfs(x,y-1)

            return val+l+r+u+d
            
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    if dfs(i,j)%k==0:
                        ans+=1

        return ans
        