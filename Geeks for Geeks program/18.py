#User function Template for python3

def nonNegativeAverage(arr):
    
    #Write your code to find average of positive numbers in number list
    #Return the answer
    ans=[]
    for i in arr:
        if i>=0:
            ans.append(i)
    
    total=0
    for j in ans:
        total+=j
    
    avg=total/len(ans)
    return avg
            
            