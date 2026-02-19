
"""Set Operations
Difficulty: BasicAccuracy: 57.93%Submissions: 21K+Points: 1
You are given an array arr[] of size n. You have to insert all elements of arr[] into a set and return that set .You are also given a interger x. If x is found in set then erase it from set and print "erased x", otherwise, print "not found".
Note: Only complete setDisplay() method, do not print the set yourself — the driver will handle printing.

Example 1:

Input: n = 10, arr[] = 9 8 7 4 4 2 1 1 9 8, x = 1
Output: 
1 2 4 7 8 9
erased 1
2 4 7 8 9
Constraints:
1 ≤ n ≤ 103
1 ≤ arr[i] ≤ 106

"""

def setInsert(arr, n):
    #code here
    s=set()
    for i in arr:
        s.add(i)
    return s
    
def setDisplay(s):
    #code here
    for j in sorted(s):
        print(j,end=" ")
    print()

def setErase(s, x):
    if x in s:
        s.discard(x)
        print("erased",x)
    else:
        print("not found")
        
    #code here
