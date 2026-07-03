from collections import defaultdict
import heapq
from typing import List, Tuple

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        def dijkstra(n, src, target, mid, k, adj):
            dist = [float('inf')] * n
            dist[src] = 0
            pq = [(0, src)]

            while pq:
                curr_dist, u = heapq.heappop(pq)

                if curr_dist > dist[u]:
                    continue
                if not online[u]:  # Skip offline nodes
                    continue
                if curr_dist > k:
                    continue
                if u == target:
                    return True

                for v, wt in adj[u]:
                    if not online[v]:  # Skip offline neighbors
                        continue
                    if wt < mid:
                        continue
                    if curr_dist + wt > k:
                        continue
                    if curr_dist + wt < dist[v]:
                        dist[v] = curr_dist + wt
                        heapq.heappush(pq, (dist[v], v))
            return False

        # If source or target is offline, impossible
        n = len(online)
        if not online[0] or not online[n - 1]:
            return -1

        # Build graph
        g = defaultdict(list)
        maxi = 0
        for u, v, w in edges:
            g[u].append((v, w))
            maxi = max(maxi, w)

        l, h = 0, maxi
        ans = -1

        # Binary search over possible 'mid' values
        while l <= h:
            mid = (l + h) // 2
            if dijkstra(n, 0, n - 1, mid, k, g):
                ans = mid
                l = mid + 1
            else:
                h = mid - 1

        return ans
