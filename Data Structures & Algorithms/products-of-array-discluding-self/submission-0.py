class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        maxProduct = 1
        output = []
        zeroPosition = []

        #figure out the highest product
        for i in range(len(nums)):
            if nums[i] != 0:
                maxProduct = maxProduct * nums[i]
            else:
                zeroPosition.append(i)

        for i in range(len(nums)):
            if len(zeroPosition) > 1:
                output.append(0)
            elif len(zeroPosition) == 1:
                if nums[i] == 0:
                    output.append(maxProduct)
                else:
                    output.append(0)
            else:
                output.append(maxProduct // nums[i])

        return output