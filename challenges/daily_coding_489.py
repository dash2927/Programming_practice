'''
 Problem [EASY]
 --------------

 This problem was asked by Google.

 Given an array of elements, return the length of the longest subarray where
 all its elements are distinct.

 For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest
 subarray of distinct elements is [5, 2, 3, 4, 1].

'''
array = [5, 1, 3, 5, 2, 3, 4, 1]

def longest_subarray(arr):
    s = {}
    longest = []
    cnt = 0
    for i in arr:
        if i in longest:
            pos = s[i]
            for j in s.keys():
                if s[j] <= pos:
                    s[j] = None
                    longest.remove(j)
        longest += [i]
        s[i] = cnt
    return longest
