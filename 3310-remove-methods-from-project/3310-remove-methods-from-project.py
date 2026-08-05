class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        indegre=[0]*n
        adj=[[]for _ in range(n)]
        for i in invocations:
            u,v=i[0],i[1]
            adj[u].append(v)
            indegre[v]+=1

        sus=set()
        def dfs(node):
            sus.add(node)
            for nbg in adj[node]:
                indegre[nbg]-=1
                if nbg not in sus:
                    dfs(nbg)

        dfs(k)
        
        for node in sus:
            if indegre[node]:
                return list(range(n))

        return [node for node in range(n) if not node in sus]