class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = digits[-1]
        
        if len(digits) > 1:
            for i in range(-2, -len(digits) -1, -1):
                if i < -1:
                    res += digits[i] * (10 ** abs(i + 1))
        res += 1

        new_digits = []
        for i in str(res):
            new_digits.append(int(i))

        return new_digits