"""Find Pattern
Difficulty: BasicAccuracy: 63.48%Submissions: 30K+Points: 1
Given a string s, and a pattern p. You need to find if p exists in s or not and return the starting index of p in s. If p does not exist in s then -1 will be returned.
Here p and s both are case-sensitive.

Examples:

Input: s = "Hello", p = "llo"
Output: 2
Explanation: llo starts from the second index in Hello.
Input: s = "World", p = "Doodle"
Output: -1
Explanation: Both are different."""

def isPalindrome(s):
    #code here
    s=s.lower()
    if s==s[::-1]:
        return True
    else:
        return False
    
    