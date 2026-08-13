class Twitter:

    def __init__(self):
        self.followers=defaultdict(set)
        self.tweets=defaultdict(list)
        self.count=0
    
    def merge_k_sorted_list(self, lst):
        heap = []
        ans = []

        for i in range(len(lst)):
            j = len(lst[i]) - 1
            heapq.heappush(heap, (lst[i][j], i, j))

        while heap and len(ans) < 10:

            val, i, j = heapq.heappop(heap)

            cnt, t_id = val
            ans.append(t_id)

            if j - 1 >= 0:
                heapq.heappush(
                    heap,
                    (lst[i][j-1], i, j-1)
                )

        return ans
            

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count-1,tweetId))
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        temp=[]
        #list of tweets of user himself
        lst=self.tweets[userId]
        if lst:
            temp.append(lst)

        #lst of tweets posted by users followd by user
        for u in self.followers[userId]:
            
            lst=self.tweets[u]
            if lst:
                temp.append(lst)


        return self.merge_k_sorted_list(temp)

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)