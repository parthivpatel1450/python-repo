def findPattern(s,p):
    #code here
    if p in s:
        return s.find(p) 
    else:
        return -1