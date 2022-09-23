n1 = 23456
n2= 23455

# AND

print(bin(n1)[2:])
print(bin(n2)[2:])
print(bin(n1&n2)[2:], n1&n2)

# OR
print(bin(n1|n2)[2:], n1|n2)

# XOR
print(bin(n1^n2)[2:], n1^n2)

# NOT
print(bin(0b111111111111111-10)[2:], bin(10)[2:] )

number = 32
# shifting left mean multiplying by 2

print(bin(number)[2:])
number <<= 1
print(bin(number)[2:])
print(number)

# shifting right mean dividing by 2
number >>= 1 
print(number)


