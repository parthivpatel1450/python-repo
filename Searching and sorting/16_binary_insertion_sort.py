import bisect

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = bisect.bisect_left(arr, key, 0, i)
        arr = arr[:j] + [key] + arr[j:i] + arr[i + 1:]
    return arr

arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
print("Original:", arr)
print("Sorted:", binary_insertion_sort(arr[:]))
