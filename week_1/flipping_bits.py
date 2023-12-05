"""
You will be given a list of 32 bit unsigned integers. Flip all the bits (1 -> 0 and 0 -> 1) and return the result as an unsigned integer.

#Example
n = 9^10
9^10 = 1001^2

00000000000000000000000000001001^2 = 9^10
11111111111111111111111111110110^2 = 4294967286^10

return 4294967286
"""

#convert to 32 bit integer and minus N
def flippingBits(n):
    return int('1' * 32, 2) - n