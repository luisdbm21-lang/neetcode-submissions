class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already = []
        for n in nums:
            if n in already:
                return True
            else:
                already.append(n)
        return False