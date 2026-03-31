"""
 Please write a program which prints all permutations of [1,2,3]
"""

from itertools import permutations

nums = [1, 2, 3]

perms = permutations(nums)

for p in perms:
    print(list(p))