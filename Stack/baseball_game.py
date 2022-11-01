"""
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
"""


def baseball_game(operations):
    # insertion and delection at the end
    stack = []
    for op in operations:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    stack_sum = sum(stack)
    return stack_sum


operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print(baseball_game(operations))
