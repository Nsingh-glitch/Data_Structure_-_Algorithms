import bisect
import math
from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        def count_pair(x):
            cnt = 0

            for a in nums1:
                if a > 0:
                    target = x // a
                    cnt += bisect.bisect_right(nums2, target)

                elif a < 0:
                    target = math.ceil(x / a)
                    idx = bisect.bisect_left(nums2, target)
                    cnt += len(nums2) - idx

                else:  # a == 0
                    if x >= 0:
                        cnt += len(nums2)

            return cnt

        p1 = nums1[0] * nums2[0]
        p2 = nums1[0] * nums2[-1]
        p3 = nums1[-1] * nums2[0]
        p4 = nums1[-1] * nums2[-1]

        l = min(p1, p2, p3, p4)
        h = max(p1, p2, p3, p4)

        while l <= h:
            mid = (l + h) // 2

            if count_pair(mid) < k:
                l = mid + 1
            else:
                h = mid - 1

        return l