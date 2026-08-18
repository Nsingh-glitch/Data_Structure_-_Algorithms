class Solution:
    def carPooling(self, trips: List[List[int]], cap: int) -> bool:
        n=len(trips)
        tmp=[]
        for i in range(n):
            x,y,z=trips[i]
            tmp.append((y,x))
            tmp.append((z,-x))
        tmp.sort()

        cnt=0
        for i in tmp:
            x,y=i
            cnt+=y
            if cnt>cap:
                return False

        return True
                    