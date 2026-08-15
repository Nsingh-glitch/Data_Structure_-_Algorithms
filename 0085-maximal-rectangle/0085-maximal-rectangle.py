class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:

        def func(arr):

            st=[]
    
            n=len(arr)
            prfx=[-1]*n
            suffx=[n]*n


            st=[0]
            for i in range(1,n):
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                if st :
                    prfx[i]=st[-1]

                st.append(i)

            st=[n-1]
            for i in range(n-2,-1,-1):
                while st and arr[st[-1]]>arr[i]:
                    st.pop()
                if st :
                    suffx[i]=st[-1]

                st.append(i)

        

            ans=0
            for i in range(n):
                p=suffx[i]-prfx[i]-1
            

                ans=max(ans,p*arr[i])
                print(ans,arr[i],prfx[i],suffx[i])

            return ans
        m=len(mat)
        n=len(mat[0])

        temp=[0]*n
        ans=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]=="0":
                    temp[j]=0
                else:
                    temp[j]+=int(mat[i][j])

            ans=max(ans,func(temp))        

        return ans