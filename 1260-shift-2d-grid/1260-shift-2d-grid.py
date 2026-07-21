class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        N=m*n
        k%=N
        if not k:return grid

        def shift(i,j):
            while i<=j:
                grid[i//n][i%n] , grid[j//n][j%n] = grid[j//n][j%n] , grid[i//n][i%n]
                i+=1
                j-=1




        shift(0,N-1)
        shift(0,k-1)
        shift(k,N-1)
        return grid


        '''this one is better apporoach direclty applying 1-d rotation logic
            on 2-d grid converting each 1-d ind in 2-d indices
            TC: O(m*n)
            SC: O(1)
        '''