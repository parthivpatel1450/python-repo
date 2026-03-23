"""
Question : A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 
The numbers after the direction are steps. 
Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer. 
Example: If the following tuples are given as input to the program:
UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2 

"""


def distance(a):
    UP=0
    DOWN=0
    LEFT=0
    RIGHT=0
    b=a.split()
    for i in range(0,len(b),2): 
        if b[i]=="UP":
            UP+=int(b[i+1])
        elif b[i]=="DOWN":
            DOWN+=int(b[i+1])
        elif b[i]=="LEFT":
            LEFT+=int(b[i+1])
        elif b[i]=="RIGHT":
            RIGHT+=int(b[i+1])
        else:
            pass
    d=int(((((UP - DOWN) ** 2) + ((LEFT - RIGHT) ** 2))  ** 0.5))
    return d
a=input("Enter Positions like UP 5 DOWN 3 LEFT 3 RIGHT 2 : ")
print(distance(a))







