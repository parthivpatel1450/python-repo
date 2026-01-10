def list_contain_even(l):
    for element in l:
        if element%2==0:
            print("list contain even element")
            break
    else:
        print("list not contain even element")

print("list no .1")
list_contain_even([1,9,8])
print("list no .2")
list_contain_even([1,3,5,7])
    
        