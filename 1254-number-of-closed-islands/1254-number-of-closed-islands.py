class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        def dfs(x,y):
            if x<0 or x>=m or y<0 or y>=n:
                return False

            if  grid[x][y]==1:
                return True

            grid[x][y]=1

            u=dfs(x+1,y)
            d=dfs(x-1,y)
            l=dfs(x,y+1)
            r=dfs(x,y-1)
            
            return u and d and l and r

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    if dfs(i,j):
                        ans+=1

        return ans
    
        