class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans=''
        fact=1
        numbers=[]
        for i in range(1,n):
            fact*=i
            numbers.append(i)

        numbers.append(n)
        k-=1
        
        while True:
            ele=numbers[k//fact]
            ans+=str(ele)
            numbers.remove(ele)

            if len(numbers)==0:return ans

            k%=fact
            fact=fact//len(numbers)

        return -1



            

