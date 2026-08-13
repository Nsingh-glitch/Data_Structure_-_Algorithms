class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap=dict()

        for i in range(len(nums)):
            hmap[nums[i]]=hmap.get(nums[i],0)+1

        freq = [[] for _ in range(len(nums) + 1)]
        for n, f in hmap.items():
            freq[f].append(n)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res