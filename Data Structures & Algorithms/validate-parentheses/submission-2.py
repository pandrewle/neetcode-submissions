class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dct = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if stack and stack[-1] in dct.values():
                return False
            if stack and c == dct[stack[-1]]:
                stack.pop()
            else:
                stack.append(c)
                print(stack)
        return not stack
    