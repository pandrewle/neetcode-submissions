from collections import deque, defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        # self.maxHeap = []
        self.queue = deque()
        self.data = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.data[userId].add(userId)
        meta = (self.time, tweetId, userId)
        self.queue.append(meta)

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        count = 0
        for event in reversed(self.queue):
            if count == 10:
                break
            if event[2] in self.data[userId]:
                feed.append(event[1])
                count += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.data[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.data[followerId].discard(followeeId)