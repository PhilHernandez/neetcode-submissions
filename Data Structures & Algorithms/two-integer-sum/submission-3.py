class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            if nums[i] not in dct.keys():
                dct[nums[i]] = [i]
            else:
                dct[nums[i]].append(i)

            jalue = target - nums[i]
            if jalue in dct.keys() and len(dct[jalue]) >= 2:
                return dct[jalue][0:2]
            elif jalue in dct.keys() and jalue != nums[i]:
                return dct[jalue] + dct[nums[i]]

#{3:[0],4:[1],5:[2],6:[3]}
            

