def rotate_by_one(arr):
    if not arr:
        return arr
    last = arr[-1]
    return [last] + arr[:-1]
arr = [11, 22, 33, 44, 55]
rotated = rotate_by_one(arr)
print("Rotated array:", rotated)
