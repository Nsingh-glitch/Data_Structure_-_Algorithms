import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []  # right side (larger half)
        self.max_heap = []  # left side (smaller half, negative values)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        # maintain order: max_heap top <= min_heap top
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # balance sizes
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2