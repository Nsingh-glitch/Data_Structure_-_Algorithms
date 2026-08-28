class Solution:
    ans=""

    def solve(self,ind,greater,res,alpha,target,n,midd):
        if ind==n:
            left="".join(res)
            right=left[::-1]
            palindrome=left+midd+right
            if palindrome>target:
                self.ans=palindrome
                return True
            
            return False

        for i in range(0,26):
            if alpha[i]==0 :continue

            if not greater and chr(i+ord('a'))<target[ind]:
                continue

            res.append(chr(i+ord('a')))
            alpha[i]-=1

            is_greater=greater or chr(i+ord('a'))>target[ind]

            if self.solve(ind+1,is_greater,res,alpha,target,n,midd):
                return True

            res.pop()
            alpha[i]+=1

        return False

    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        alpha=[0]*26
        for i in s:
            alpha[ord(i)-ord('a')]+=1

      
        midd=""
        for j in range(26):
            if alpha[j]%2==1:
                if midd:return ""

                midd=chr(ord('a')+j)
            alpha[j]=alpha[j]//2
            
        n=len(s)//2
        self.solve(0,False,[],alpha,target,n,midd)


        return self.ans

        