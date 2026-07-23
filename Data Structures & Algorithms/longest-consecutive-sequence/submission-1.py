class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #iterate through list once, store each value in hash
        #ignore duplicates
        #find the highest number and work backwards
        hashArr = set()
        for i in range(len(nums)):
            if nums[i] not in hashArr:
                hashArr.add(nums[i])

        seqStarters = set()
        #find seq starters
        for i in range(len(nums)):
            if (nums[i] - 1) not in hashArr and nums[i] not in seqStarters:
                seqStarters.add(nums[i])

        maxConsecLen = 0
        seqCount = 0
        for nums in seqStarters:
            i=0
            while (nums + i) in hashArr:
                seqCount+=1
                i+=1
            if seqCount > maxConsecLen:
                maxConsecLen = seqCount
            seqCount = 0

        return maxConsecLen