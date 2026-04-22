class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] = 1 + hm[num]
            else:
                hm[num] = 1
        bucket = [[] for i in range(len(nums))]
        topKFrequent = []
        for num, value in hm.items():
            bucket[value-1].append(num)
            for num in bucket:
                print(num)
        for i in range(len(bucket)):
            most_frequent = len(bucket) - i - 1
            if bucket[most_frequent]:
                topKFrequent.extend(bucket[most_frequent])
                if len(topKFrequent) == k:
                    return topKFrequent
        





