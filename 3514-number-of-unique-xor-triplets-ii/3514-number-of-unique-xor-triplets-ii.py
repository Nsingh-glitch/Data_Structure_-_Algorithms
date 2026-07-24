class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n==0 or n==1:return n
        s=set()
        T=set()
        for i in range(n):
            for j in range(i+1,n):
                s.add(nums[i]^nums[j])
        s=list(s)
        for i in range(n):
            for k in range(len(s)):
                T.add(nums[i]^s[k])



        return len(T)