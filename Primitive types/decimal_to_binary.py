'''
    Recurcive approach
    complexity o(log n)
'''

import math
result = []
def int_to_binary(n: int) -> int:
    if n:
        remainder = n%2
        Q = math.floor(n/2)
        int_to_binary(Q)
    else: 
        return 
    result.append(str(remainder))
    
    return "".join(result)
a = int_to_binary(46)
print(a)