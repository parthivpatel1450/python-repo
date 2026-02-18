def isPalindrome(s):
    #code here
    s=s.lower()
    if s==s[::-1]:
        return True
    else:
        return False
    
    