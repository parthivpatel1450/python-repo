import copy
# Original list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Creating a shallow copy
shallow_copied_list = copy.copy(original_list)
shallow_copied_list[0][0]=100
print(original_list)
print(shallow_copied_list)