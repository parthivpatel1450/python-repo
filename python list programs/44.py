import copy
# Original list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Creating a deep copy
deep_copied_list = copy.deepcopy(original_list)
# Modifying an element in the deep copied list
deep_copied_list[0][0] = 100
# Printing both lists
print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)