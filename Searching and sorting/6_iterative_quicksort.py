def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def iterative_quicksort(arr, low, high):
    stack = []
    stack.append((low, high))
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

arr = [10, 7, 8, 9, 1, 5]
print("Original:", arr)
iterative_quicksort(arr, 0, len(arr) - 1)
print("Sorted:", arr)
