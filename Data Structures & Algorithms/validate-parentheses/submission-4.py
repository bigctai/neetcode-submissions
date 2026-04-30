class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False
                match = stack.pop()
                if char == ")" and match != "(":
                    return False
                elif char == "]" and match!= "[":
                    return False
                elif char == "}" and match!= "{":
                    return False
        if not stack:
            return True
        else:
            return False

