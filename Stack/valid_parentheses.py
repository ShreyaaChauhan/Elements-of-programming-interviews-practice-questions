"""Input: s = "()[]{}"
Output: true"""


def valid_parentheses(str):
    stack = []
    Map = {")": "(", "]": "[", "}": "{"}
    for c in str:
        if c in Map:
            if stack and stack[-1] == Map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


s = "["
print(valid_parentheses(s))
