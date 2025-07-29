def printDiagonalSums(mat, n):
    principal = 0
    secondary = 0;
    for i in range(0, n): 
        for j in range(0, n): 
            if (i == j):
                principal += mat[i][j]
            if ((i + j) == (n - 1)):
                secondary += mat[i][j]       
    print("Principal Diagonal:", principal)
    print("Secondary Diagonal:", secondary)
s = [[ 11, 22, 33, 44 ],
     [ 55, 66, 77, 88 ], 
     [ 10, 20, 31, 42 ],
      [ 5, 6, 77, 80 ]]
printDiagonalSums(s, 4)
# Output :- 
# Principal Diagonal: 188
# Secondary Diagonal: 146
