class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        already = []
        k = len(nums)
        for i in range(len(nums)):
            if nums[i] in already:
                nums[i] = 999
                k -= 1
            else:
                already.append(nums[i])
        nums.sort()
        return k