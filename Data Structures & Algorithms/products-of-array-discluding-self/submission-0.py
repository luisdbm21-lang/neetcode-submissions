class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_list = []
        for i in range(len(nums)):
            a = "initial"
            for j in range(len(nums)):
                if i != j:
                    if a == "initial":
                        a = nums[j]
                    else:
                        a = a * nums[j]
            result_list.append(a)
        
        return result_list
