class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Start by initializing the variables and the last element value. These two variables are used for the 
        curr_greatest_element = arr[-1]
        next_greatest_element = curr_greatest_element
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            next_greatest_element = max(arr[i], curr_greatest_element)
            arr[i] = curr_greatest_element
            curr_greatest_element = next_greatest_element

        return arr