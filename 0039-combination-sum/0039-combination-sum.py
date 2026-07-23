class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(arr)
        def x(i,temp,st):
            if temp<0:return

            if i==n:
                if temp==0:
                    ans.append(st[:])
                return

            x(i+1,temp,st)

            if arr[i]<=target:
                st.append(arr[i])
                x(i,temp-arr[i],st)
                st.pop()
            return

        x(0,target,[])
        return ans
        