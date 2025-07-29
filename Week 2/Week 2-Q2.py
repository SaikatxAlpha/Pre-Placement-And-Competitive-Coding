def rotate90(mat):
    n = len(mat)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n - i - 1] = mat[i][j]
    for i in range(n):
        for j in range(n):
            mat[i][j] = res[i][j]
mat = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
]
rotate90(mat)
for row in mat:
    print(" ".join(map(str, row)))

# Output :- 130 90 50 10
# 140 100 60 20
# 150 110 70 30
# 160 120 80 40