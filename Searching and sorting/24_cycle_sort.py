def cycle_sort(arr):
    writes = 0
    n = len(arr)
    for cycle_start in range(n - 1):
        item = arr[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            writes += 1
    return arr, writes

arr = [1, 8, 3, 9, 10, 10, 2, 4]
print("Original:", arr)
sorted_arr, writes = cycle_sort(arr[:])
print("Sorted:", sorted_arr)
print("Total writes:", writes)
