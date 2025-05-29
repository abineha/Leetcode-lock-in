from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.count = 0  # timestamp of twt, decrease it so newer tweets have a smaller (more negative) value, helping with the min-heap
        self.tweetmap = defaultdict(list)   # userId -> list of [ count, tweetIds ]
        self.followMap = defaultdict(set)   # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])   # Appends tweet to the user's tweet list
        self.count -=1  # minheap to get recent so -ve, decreasing count to keep track of time ordering        

    def getNewsFeed(self, userId: int) -> list[int]:
        result = []     # ordering from recent
        minHeap = []
        self.followMap[userId].add(userId)  # follower of oneself -> edge case

        # For each user followed (including themselves)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetmap:
                index = len(self.tweetmap[followeeId]) - 1   # index points to the last tweet in the list (most recent)
                count, tweetId = self.tweetmap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(minHeap)
        while minHeap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            result.append(tweetId)
            #  if the followee has older tweets, push the next most recent tweet into the heap
            if index >= 0:
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minHeap, [count,tweetId, followeeId, index - 1])
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# import heapq
# from collections import defaultdict
# from typing import List

# class Twitter:

#     def __init__(self):
#         self.count = 0  
#         self.posts = defaultdict(list)  
#         self.followers = defaultdict(set)  

#     def postTweet(self, userId: int, tweetId: int) -> None:
       
#         self.posts[userId].append((self.count, tweetId))
#         self.count -= 1

#     def getNewsFeed(self, userId: int) -> List[int]:
#         heap = []
      
#         self.followers[userId].add(userId)

#         for followeeId in self.followers[userId]:
#             for tweet in self.posts[followeeId]: 
#                 heapq.heappush(heap, tweet)
                
#         res = []
#         count=0
#         while heap:
#             if(count>=10):
#                 break
#             res.append(heapq.heappop(heap)[1])  
#             count=count+1
#         return res 

#     def follow(self, followerId: int, followeeId: int) -> None:
#         #if followerId != followeeId:
#             self.followers[followerId].add(followeeId)

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         if followeeId in self.followers[followerId]:
#             self.followers[followerId].remove(followeeId)



# # Your Twitter object will be instantiated and called as such:
# # obj = Twitter()
# # obj.postTweet(userId,tweetId)
# # param_2 = obj.getNewsFeed(userId)
# # obj.follow(followerId,followeeId)
# # obj.unfollow(followerId,followeeId)