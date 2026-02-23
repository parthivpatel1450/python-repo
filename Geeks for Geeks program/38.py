"""Merge two binary Max heaps
Difficulty: EasyAccuracy: 58.65%Submissions: 59K+Points: 2
Given two binary max heaps as arrays, merge the given heaps to form a new max heap.

 

Example 1:

Input  : 
n = 4 m = 3
a[] = {10, 5, 6, 2}, 
b[] = {12, 7, 9}
Output : 
{12, 10, 9, 2, 5, 7, 6}
Explanation :




 """

#User function Template for python3
import heapq
class Solution():
    def mergeHeaps(self, a, b, n, m):
        #your code here
        a.extend(b)
        heapq._heapify_max(a)
        return a
        
        
        

        

