"""
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

#Example
strings = ['ab','ab','abc']
queries = ['ab','abc','bc']

There are 2 instances of 'ab', 1 of 'abc' and 0 for 'bc'. For each query, add an element to the return array.
results = [2,1,0]
"""

#return count of matches between strings and queries
def matchingStrings(strings, queries):
    return [strings.count(i) for i in queries]