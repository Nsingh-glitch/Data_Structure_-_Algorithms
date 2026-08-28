class Solution:
    ans=""
    
    #now we try to make permutation just greater than target
    #we will try to find letter >= for every ith element
    def solve(self,ind,greater,res,alpha,target,n):
        if ind==n:
            if greater:
                self.ans=''.join(res)
                return True
            return False

        for i in range(0,26):
            if alpha[i]==0 :continue

            if not greater and chr(i+ord('a'))<target[ind]:
                continue

            res.append(chr(i+ord('a')))
            alpha[i]-=1

            is_greater=greater or chr(i+ord('a'))>target[ind]

            if self.solve(ind+1,is_greater,res,alpha,target,n):
                return True

            res.pop()
            alpha[i]+=1

        return False

    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n=len(s)
        alpha=[0]*26
        for i in s:
            alpha[ord(i)-ord('a')]+=1

        self.solve(0,False,[],alpha,target,n)
        return self.ans

                



            




