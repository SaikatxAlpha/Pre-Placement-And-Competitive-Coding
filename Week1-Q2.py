def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [9996, 9997, 9998, 9999, 9801]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)

#Output :- 9999