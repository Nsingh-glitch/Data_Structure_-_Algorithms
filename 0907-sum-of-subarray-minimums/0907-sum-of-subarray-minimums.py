class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st=[]
        mod=1000000000+7
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
            p1=i-prfx[i]
            p2=suffx[i]-i
            ans+=p1*p2*arr[i]

        return ans%mod