class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_element = arr[-1]
        next_greatest_element = greatest_element
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            next_greatest_element = max(arr[i], greatest_element)
            arr[i] = greatest_element
            greatest_element = next_greatest_element
            
        return arr