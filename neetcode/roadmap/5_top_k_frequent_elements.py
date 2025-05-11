class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}

        for i in nums:
            d[i]=1+d.get(i,0)

        # bucket sort
        
        freq= [[] for _ in range(len(nums)+1)]

        for key,value in d.items():
            freq[value].append(key)

        res=[]

        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
                
if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))