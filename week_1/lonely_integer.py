"""
Given an array of integers, where all elements but one occur twice, find the unique element.

#Example
a = [1,2,3,4,3,2,1]
unique element is 4
"""

#loop through list and count unique elements
#return the one unique element
def lonelyInteger(a):
    unique = [i for i in a if a.count(i) == 1]
    return unique.pop()