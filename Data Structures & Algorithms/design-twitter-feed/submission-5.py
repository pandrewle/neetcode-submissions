from collections import deque, defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.userTweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.following[userId].add(userId)

        meta = (self.time, tweetId)
        self.userTweets[userId].append(meta)

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for followee in self.following[userId]:
                for tweet in reversed(self.userTweets[followee][-10:]):
                    if len(feed) < 10:
                        heapq.heappush(feed, (tweet[0],tweet[1]))
                    elif tweet[0] >= feed[0][0]:
                        heapq.heappop(feed)
                        heapq.heappush(feed, tweet)
                    else:
                        break
        res = []                
        while feed:
            res.append(heapq.heappop(feed)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)