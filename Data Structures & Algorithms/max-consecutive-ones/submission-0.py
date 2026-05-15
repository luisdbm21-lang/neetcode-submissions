class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret, counter = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
                ret = max(ret, counter)
            else:
                counter = 0
        
        return ret