class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                maxi = arr[i+1]
                for j in range(i+1, len(arr)):
                    if maxi < arr[j]:
                        maxi = arr[j]
                arr[i] = maxi
        return arr