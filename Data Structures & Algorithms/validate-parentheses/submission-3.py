class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for i in range(len(s)):
            if s[i] == ")":
                if brackets:
                    if brackets[-1] != "(":
                        return False
                    else:
                        brackets.pop()
                else:
                    return False
            elif s[i] == "}":
                if brackets:
                    if brackets[-1] != "{":
                        return False
                    else:
                        brackets.pop()
                else:
                    return False
            elif s[i] == "]":
                if brackets:
                    if brackets[-1] != "[":
                        return False
                    else:
                        brackets.pop()
                else:
                    return False
            elif s[i] == "(":
                brackets.append("(")
            elif s[i] == "{":
                brackets.append("{")
            elif s[i] == "[":
                brackets.append("[")
        if len(brackets) != 0:
            return False
        else:
            return True