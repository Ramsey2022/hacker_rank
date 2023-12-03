# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# example
"""
arr = [1,3,5,7,9]
min_sum is 1 + 3 + 5 + 7 = 16
max_sum is 3 + 5 + 7 + 9 = 24

function prints 16 24
"""

def miniMaxSum(arr):
    add = []
    array_one = sum(arr) - arr[0]
    array_two = sum(arr) - arr[1]
    array_three = sum(arr) - arr[2]
    array_four = sum(arr) - arr[3]
    array_five = sum(arr) - arr[4]
    add.append(array_one)
    add.append(array_two)
    add.append(array_three)
    add.append(array_four)
    add.append(array_five)
    max_sum = max(add)
    min_sum = min(add)
    
    print(min_sum, max_sum)