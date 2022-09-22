'''
    complexity = o(n)
    minor change
'''
def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x>>=1
    return num_bits
    
no_of_bits = count_bits(10)
print(no_of_bits)