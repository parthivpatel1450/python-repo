
def pigeonhole_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1
    holes = [0] * size
    for x in arr:
        holes[x - min_val] += 1
    result = []
    for i, count in enumerate(holes):
        result.extend([i + min_val] * count)
    return result

arr = [8, 3, 2, 7, 4, 6, 8]
print("Original:", arr)
print("Sorted:", pigeonhole_sort(arr))
