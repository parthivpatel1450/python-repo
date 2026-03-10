def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

arr = [2, 3, 4, 10, 40, 100, 20]
target = 10
print("Array:", arr)
print(f"Linear search for {target}: index {linear_search(arr, target)}")

target2 = 99
print(f"Linear search for {target2}: index {linear_search(arr, target2)}")
