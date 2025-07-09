def matrix_transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    return matrix

    


matrix=[[1,2,3],[4,5,6],[7,8,9]]

final=matrix_transpose(matrix)

print("The transpose of the matrix is:")
for i in range(len(final)):
    for j in range(len(final[0])):
        print(final[i][j],end=' ')
    print()

