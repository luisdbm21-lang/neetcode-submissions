class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        word_length = 0

        for i in range(n-1, -1, -1):
            if s[i] != " ":
                word_length += 1
            elif s[i] == " " and word_length > 0:
                return word_length
            
        return word_length