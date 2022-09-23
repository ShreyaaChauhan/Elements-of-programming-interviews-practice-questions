'''
    using recursive approach
    complexity o(log n)
'''
import math
COUNT = 0
def parity_check(n: int) -> int:
    global COUNT
    if n:
        remainder = n%2
        if remainder == 1:
            COUNT +=1
        Q = math.floor(n/2)
        parity_check(Q)
    else: 
        return 
    if COUNT%2==0:
        return 0
    return 1
    

print("Parity",parity_check(10))
    