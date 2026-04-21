class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()

        for n in nums:
            if n not in uniques:
                uniques.add(n)
            else:
                return True
        
        return False