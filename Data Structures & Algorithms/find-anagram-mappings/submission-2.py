class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        anagram_mappings = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    anagram_mappings.append(j)
                    break
        return anagram_mappings