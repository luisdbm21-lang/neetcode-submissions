class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        append_characters = len(t)
        i, j = 0, 0

        while j < len(s):
            if t[i] == s[j]:
                append_characters -= 1
                if append_characters == 0:
                    return append_characters
                else:
                    i += 1
                    if i == len(s):
                        return append_characters
            j += 1
        return append_characters