class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': lambda val1, val2: val1 + val2,
            '-': lambda val1, val2: val1 - val2,
            '*': lambda val1, val2: val1 * val2,
            '/': lambda val1, val2: val1 / val2,
        }
        stack = []
        for token in tokens:
            if token in ops.keys():
                print(stack)
                val2 = stack.pop()
                print(stack)
                val1 = stack.pop()
                res = ops[token](int(val1), int(val2))
                stack.append(res)
            else:
                stack.append(token)
        return int(stack[-1])