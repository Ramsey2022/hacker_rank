"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

#Example
arr = [1,1,0,-1,-1]

There are n = 5 elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000. Results are printed as:

0.400000
0.400000
0.200000
"""

# Create arrays of Positive, Negative, and Zero elements
# Divide new array lengths by original array length
# Return Values
def plusMinus(arr):
    positive = [i for i in arr if i > 0]
    negative = [i for i in arr if i < 0]
    zero = [i for i in arr if i == 0]
    final_pos = len(positive) / len(arr)
    final_neg = len(negative) / len(arr)
    final_zero = len(zero) / len(arr)
    print(round(final_pos, 6))
    print(round(final_neg, 6))
    print(round(final_zero, 6))