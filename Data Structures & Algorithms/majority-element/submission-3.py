class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        my_dict = {}

        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        
        return max(my_dict, key=my_dict.get)