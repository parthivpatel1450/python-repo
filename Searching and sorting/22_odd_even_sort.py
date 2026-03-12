def odd_even_sort(arr):
    n = len(arr)
    sorted_ = False
    while not sorted_:
        sorted_ = True
        # Odd phase
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_ = False
        # Even phase
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_ = False
    return arr

arr = [34, 2, 10, -9, 15, 7]
print("Original:", arr)
print("Sorted:", odd_even_sort(arr[:]))
