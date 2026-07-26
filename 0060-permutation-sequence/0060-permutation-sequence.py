class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k-=1
        nums=[]
        N=math.factorial(n)
        k%=N

        for i in range(n):
            nums.append(i+1)

        if not k:return ''.join(map(str, nums))

        def next_permut(arr):
            dip_ind=-1
            for i in range(n-2,-1,-1):
                if arr[i]<arr[i+1]:
                    dip_ind=i
                    break
            if dip_ind==-1:
                arr.reverse()
                return arr
            
            for i in range(n-1,-1,-1):
                if arr[i]>arr[dip_ind]:
                    temp=arr[i]
                    arr[i]=arr[dip_ind]
                    arr[dip_ind]=temp

                    break
            l=dip_ind+1
            r=n-1
            arr = arr[:l] + arr[l:r+1][::-1] + arr[r+1:]
            return arr

        for _ in range(k):
            nums=next_permut(nums)
           

        return ''.join(map(str, nums))