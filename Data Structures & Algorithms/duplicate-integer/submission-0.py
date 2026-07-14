class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashArray = {}
        for num in nums:
            if num in hashArray:
                return True
            else:
                hashArray[num] = num
        return False