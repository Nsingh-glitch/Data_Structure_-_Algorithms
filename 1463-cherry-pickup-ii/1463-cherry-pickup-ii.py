class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        nxt=[[0 for _ in range(n)]for _ in range(n)]

        for j1 in range(n):
            for j2 in range(n):
                if j1==j2:
                    nxt[j1][j1]=grid[m-1][j1]
                else:
                    nxt[j1][j2]=grid[m-1][j1]+grid[m-1][j2]


        for i in range(m-2,-1,-1):

            curr=[[0 for _ in range(n)]for _ in range(n)]

            for j1 in range(n):
                for j2 in  range(n):

                    maxi=-1e9
                    for dj1 in range(-1,2):
                        for dj2 in range(-1,2):
                            if j1==j2:
                                val=grid[i][j1]
                            else:
                                val=grid[i][j1] + grid[i][j2] 

                            if j1+dj1>=0 and j1+dj1<n and j2+dj2>=0 and j2+dj2<n:
                                val+= nxt[j1+dj1][j2+dj2]
                            else:
                                val+=-1e9

                            maxi=max(maxi,val)

                    
                    curr[j1][j2]=maxi
            nxt=curr

        return nxt[0][n-1]
                                


            
        