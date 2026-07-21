class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
        uniqueNums = {}
        for i in range(len(nums)):
            bucket.append([])

        for num in nums:
            if num not in uniqueNums:
                uniqueNums[num] = 0
                if len(bucket[uniqueNums[num]]) != 0:
                    bucket[uniqueNums[num]].append(num)
                else:
                    bucket[uniqueNums[num]] = [num]
            else:
                uniqueNums[num]+=1
                bucket[uniqueNums[num]].append(num)
        
        topKFrequent=[]
        for i in range(len(nums)-1,-1,-1):
            if len(bucket[i]) == k:
                return bucket[i]