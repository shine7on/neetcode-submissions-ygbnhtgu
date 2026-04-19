class Twitter:

    def __init__(self):
        self.tweet = {}
        self.follower = {}
        # usertweetID...., followersID, followersID....
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweet:
            self.tweet[userId].insert(0, tweetId)
        else:
            self.tweet[userId] = [tweetId]


    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.tweet)
        print(self.follower)
        isTrue = False
        res = []

        if userId in self.follower:
            followers = self.follower[userId]
            print(f'follower: {followers}')
            isTrue = True
            for follower in followers:
                for tweet in self.tweet[follower]:
                    res.append(tweet)

        # own tweet
        if userId in self.tweet:
            if res:
                print(self.tweet[userId])
                for tweet in self.tweet[userId]:
                    res.append(tweet)
            else:
                print(self.tweet)
                res = self.tweet[userId]

        if isTrue: 
            res.sort(reverse=True)
        return res if len(res) <= 10 else res[:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            pass
        elif followerId in self.follower:
            if not followeeId in self.follower[followerId]:
                self.follower[followerId].append(followeeId)
            else:
                return None
        else:
            self.follower[followerId] = [followeeId]


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            pass
        elif followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)