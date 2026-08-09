class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def check(sub):
            return sub == sub[::-1]
        def x(i,st):
            if i==len(s):
                ans.append(st[:])
                return

            for ind in range(i,len(s)):
                if check(s[i:ind+1]):
                    st.append(s[i:ind+1])
                    x(ind+1,st)
                    st.pop()

            return

        x(0,[])
        return ans
        