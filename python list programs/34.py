original_list = [1, 2, 3, 4, 5]
b=[(lambda x:x*2)(x) for x in original_list]
print(b)