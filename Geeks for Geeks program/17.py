def lessThan(arr, k):
    #code here
    ans = []
    for num in arr:
        if num<k:
            ans.append(num)
    return ans
