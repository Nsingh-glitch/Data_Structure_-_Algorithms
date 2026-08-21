class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # here we will use concept of exclusion and inclusions
        """so func(x) would give count of distinct multiples less than
            equals to x
        our goal is to find kth number where func(x)==count of distinct 
        numbers to be less than equal to k
        """
        n=len(coins)
        def lcm(a,b):
            def gcd(a, b):
                while b:
                    a, b = b, a % b
                return a
            return (a*b)//gcd(a,b)
 
        def func(x):
            all_total=0
            bitmask=1<<n
            for i in range(1,bitmask):
                total=0
                cnt=0
                l=1
                for j in range(n):
                    if ((1<<j)& i)>0:
                        cnt+=1
                        l=lcm(l,coins[j])
                total+=x//l

                if cnt%2==0:
                    total*=-1

                all_total+=total
            return all_total
                
        left=0
        right = min(coins) * k
        while left <=right:
            mid=(left+right)//2
            val=func(mid)
            if val>=k:
                right=mid-1

            else:
                left=mid+1


        return left
