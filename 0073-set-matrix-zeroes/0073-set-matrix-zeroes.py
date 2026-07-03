class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])

        upper=[1]*n
        left=[1]*m

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    upper[j]=0
                    left[i]=0

        for i in range(m):
            for j in range(n):
                if upper[j]==0 or left[i]==0:
                    matrix[i][j]=0

        return matrix