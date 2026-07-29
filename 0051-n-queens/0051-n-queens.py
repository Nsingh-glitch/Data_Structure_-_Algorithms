class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mat=[['.'for _ in range(n)]for _ in range(n)]
        ans=[]
        up_d=[0]*(2*n-1)
        low_d=[0]*(2*n-1)
        left=[0]*n

        def check(i,j,mat,up_d,low_d,left):
                return low_d[i+j]==0 and up_d[n-1+j-i]==0 and left[i]==0



        def solve(j,mat,up_d,low_d,left):
            if j==n:
                ans.append([''.join(i) for i in mat])
                return

            for i in range(n):
                if check(i,j,mat,up_d,low_d,left):
                    mat[i][j]='Q'

                    low_d[i+j]=1
                    up_d[n-1+j-i]=1
                    left[i]=1

                    solve(j+1,mat,up_d,low_d,left)

                    mat[i][j]='.'

                    low_d[i+j]=0
                    up_d[n-1+j-i]=0
                    left[i]=0

            return

        solve(0,mat,up_d,low_d,left)
        return ans

        


        