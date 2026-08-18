class Solution:
    def checkValidString(self, s: str) -> bool:
        low=0
        high=0
        for i in range(len(s)):
            if s[i]=='(':
                low+=1
                high+=1
            elif s[i]==')':
                low-=1
                high-=1
            else:
                low-=1
                high+=1

            low=max(0,low)
            if high<0:
                return False

        return low==0
        