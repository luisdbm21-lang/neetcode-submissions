class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}

        for i in range(len(nums2)):
            hashmap[nums2[i]] = i

        anagram_mappings = [0] * len(nums1)

        for i in range(len(nums1)):
            anagram_mappings[i] = hashmap[nums1[i]]
            
        return anagram_mappings