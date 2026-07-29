class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        h_map=[0]*n
        ans=[]
        def x(i,h_map,st):
            if i==n:
                if len(st)==n:
                    ans.append(st[:])
                return 
            
            for v in range(n):
                if h_map[v]==0:
                    st.append(nums[v])
                    
                    h_map[v]=1
                    x(i+1,h_map,st)
                    h_map[v]=0
                    st.pop()

            return 

        x(0,h_map,[])
        return ans