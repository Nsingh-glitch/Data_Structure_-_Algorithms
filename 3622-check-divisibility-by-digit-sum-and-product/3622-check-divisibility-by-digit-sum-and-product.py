class Solution:
    def checkDivisibility(self, n: int) -> bool:
        lst=[]
        orig=n
        while n:
            lst.append(n%10)
            n//=10
        print(lst)
        tmp=1
        for i in lst:
            tmp*=i

        tmp=sum(lst)+tmp
        return orig%tmp==0