class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(p)
        n=len(s)

        def x(i,j):
            if j==m:
                if i==n:
                    return True

                return False

            first_match=i<n and (s[i]==p[j] or p[j]=='.') 

            if j+1<m and (p[j+1]=='*'):
                n_take=x(i,j+2)

                take=first_match and x(i+1,j)
                return take or n_take
            
            else:
                return first_match and  x(i+1,j+1)

        return x(0,0)

            