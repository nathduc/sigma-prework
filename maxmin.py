def find_max_min(arr):
    max = arr[0]
    min = arr[0]
    for num in arr:
        if max < num:
            max = num
        if min > num:
            min = num
    return [min, max]


print(find_max_min([100, -100]))
