class Solution:
    def carPooling(self, trips: List[List[int]], cap: int) -> bool:
        n=len(trips)
        tmp=[0]*1001
        for i in range(n):
            x,y,z=trips[i]
            tmp[y]+=x
            tmp[z]+=-x
      

        cnt=0
        for i in tmp:
            cnt+=i
            if cnt>cap:
                return False

        return True
                    