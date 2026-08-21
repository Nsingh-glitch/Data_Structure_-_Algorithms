class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        st=[intervals[0]]
        for i in range(1,len(intervals)):
            u,v=intervals[i]

            x,y=st[-1]
            if y>=u:
                st.pop()
                st.append([x,max(v,y)])
            else:
                st.append([u,v])

        return st
        