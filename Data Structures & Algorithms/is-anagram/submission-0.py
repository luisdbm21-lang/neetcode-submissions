class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_array = []
            t_array = []
            for i in range(len(s)):
                s_array.append(s[i])
                t_array.append(t[i])
            s_array.sort()
            t_array.sort()
            if s_array == t_array:
                return True
            else:
                return False
        else:
            return False