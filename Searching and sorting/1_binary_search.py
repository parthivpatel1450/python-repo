def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

arr = [2, 3, 4, 10, 20, 40, 100]
target = 10
print("Array:", arr)
print(f"Searching for {target}:")
print("  Iterative:", binary_search_iterative(arr, target))
print("  Recursive:", binary_search_recursive(arr, target, 0, len(arr) - 1))

target2 = 15
print(f"Searching for {target2}:")
print("  Iterative:", binary_search_iterative(arr, target2))
