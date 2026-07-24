class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ele=max(nums)
        u=1
        while u<=ele:
            u<<=1
        
        ones=[False]*u
        twos=[False]*u
        thres=[False]*u

        for i in range(n):
            ones[nums[i]]=True
            for j in range(u):
                if ones[j]:
                    twos[j^nums[i]]=True


        for i in range(n):
            for k in range(u):
                if twos[k]:
                    thres[nums[i]^k]=True

        return sum(1 for b in thres if b)        