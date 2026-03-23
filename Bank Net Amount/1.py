"""
Question: Write a program that computes the net amount of a bank account based a transaction log from console input.
 The transaction log format is shown as following: D 100 W 200

D means deposit while W means withdrawal.
 Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500
"""


def banknetbalance(a):
    netbalance=0
    b=a.split()
    for i in range(0,len(b),2): 
        if b[i]=="D":
            netbalance+=int(b[i+1])
        elif b[i]=="W":
            netbalance-=int(b[i+1])
        else:
            pass
    return netbalance

a=input("Enter log Format like  D 300 D 300 W 200 D 100 : ")
print(banknetbalance(a))








