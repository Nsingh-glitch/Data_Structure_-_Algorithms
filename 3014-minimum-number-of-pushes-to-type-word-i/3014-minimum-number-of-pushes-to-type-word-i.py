class Solution:
    def minimumPushes(self, word: str) -> int:
        ans=0
        for i in range(len(word)):
            print(ans)
            if i>=24:
                ans+=4
            elif i>=16:
                ans+=3
            elif i>=8:
                ans+=2
            else:
                ans+=1

        return ans
        