"""Decimal number to binary number
Difficulty: EasyAccuracy: 55.91%Submissions: 22K+Points: 2
Given a decimal number n (positive) in string format, compute its binary string equivalent and return it. 
Note: Don't add a new line at the end.

Examples:

Input: n = 7
Output: 111
Input: n = 33
Output: 100001
"""

def findPattern(s,p):
    #code here
    if p in s:
        return s.find(p) 
    else:
        return -1