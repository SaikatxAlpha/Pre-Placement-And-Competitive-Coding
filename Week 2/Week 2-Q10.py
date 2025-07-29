def count_zeroes(mat):
    n = len(mat)
    row = n - 1
    col = 0
    count = 0
    while col < n:
        while row >= 0 and mat[row][col]:
            row -= 1
        count += (row + 1)
        col += 1
    return count
if __name__ == '__main__':
    mat = [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 2, 10, 4],
        [8, 5, 0, 0, 8],
        [9, 22, 15, 78, 91]
    ]
    print(count_zeroes(mat))

#Output :- 9