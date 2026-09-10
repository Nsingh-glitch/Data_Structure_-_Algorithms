class Solution:
    def countCommas(self, n: int) -> int:
        if n<=999:
            return 0
        ans=0
        if n<1000000 :
            ans+=n-1000+1

        else:
            ans+=999999-1000+1

            if n<1000000000:
                ans+=2*(n-1000000+1)

            else:
                ans+=2*(999999999-1000000+1)

                
                if n<1000000000000:
                    ans+=3*(n-1000000000+1)
                else:
                    ans+=3*(999999999999-1000000000+1)

                    if n<1000000000000000:
                        ans+=4*(n-1000000000000+1)
                    else:
                        ans+=4*(999999999999999-1000000000000+1)

                        if n>=1000000000000000:
                            ans+=5


        return ans

        