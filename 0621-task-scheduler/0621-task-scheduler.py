class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap=[0]*26
        time=0
        for i  in tasks:
            hmap[ord(i)-ord('A')]+=1

        heap=[]
        for i in range(26):
            if hmap[i]>0:
                heapq.heappush(heap,-hmap[i])

        while heap:
            temp=[]
            for i in range(n+1):
                if heap:
                    freq=-heapq.heappop(heap)
                    
                    freq-=1
                    temp.append(freq)

            for i in temp:
                if i>0:
                    heapq.heappush(heap,-i)

            if not heap:
                time+=len(temp)
            else:
                time+=n+1

        return time



        