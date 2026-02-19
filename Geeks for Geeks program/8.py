"""For Loop 2- Python
Difficulty: EasyAccuracy: 76.72%Submissions: 60K+Points: 2Average Time: 10m
You are given a string s, you need to print its characters at even indices(index starts at 0).

Note: Please go through the range function to understand how to jump 2 steps.

Examples:

Input: s = "DoctorPhenomenal"
Output: DcoPeoea
Input: s = "Geeks"
Output: Ges 
"""

def returnValueFunction(n):
    return n * 2

def main():
    n = int(input())
    print(returnValueFunction(n))

