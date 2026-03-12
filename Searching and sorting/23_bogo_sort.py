import random

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogo_sort(arr, max_attempts=10000):
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
        if attempts >= max_attempts:
            print(f"Stopped after {max_attempts} attempts (not practical for large arrays)")
            return arr
    print(f"Sorted after {attempts} attempts")
    return arr

arr = [3, 2, 4, 1]  # Keep small - this is O(n*n!)
print("Original:", arr)
bogo_sort(arr)
print("Sorted:", arr)
