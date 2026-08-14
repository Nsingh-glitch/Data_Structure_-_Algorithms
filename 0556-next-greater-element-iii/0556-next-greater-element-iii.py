class Solution:
    def nextGreaterElement(self, n: int) -> int:
        orig=n
        #i am converting the n into a list containing digits of n
        def func(arr,x,y):
            i=x
            j=y
            while i<j:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp

                i+=1
                j-=1
            return 
        nums=[]
        mult=10
        while n:
            nums.append(n%10)
            n//=10
        nums.reverse()
        if len(nums)<=1:
            return -1

        ind=-1

        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                for j in range(len(nums)-1,-1,-1):
                    if nums[j]>nums[i]:
                        temp=nums[j]
                        nums[j]=nums[i]
                        nums[i]=temp

                        break
                ind=i

                break
        if ind == -1:
            return -1

        func(nums, ind + 1, len(nums) - 1)

        ans = 0
        mult = 1

        for i in range(len(nums) - 1, -1, -1):
            ans += nums[i] * mult
            mult *= 10

        if ans > 2**31 - 1:
            return -1

        return ans