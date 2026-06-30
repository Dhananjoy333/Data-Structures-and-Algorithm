#Iteration over 2D matrix
mat = [[1,2,3],[4,5,6],[7,8,9]]
def iterate(mat):
    rows = len(mat)
    cols = len(mat[0])
    for i in range(0,rows):
        for j in range(0,cols):
            print(mat[i][j],end=" ")
        print()


#Print only the upper triangle and change all lower value to *
# def upperTri(mat):
#     rows = len(mat)
#     cols = len(mat[0])
#     for i in range(0,rows):
#         for j in range(0,cols):
#             if j >= i:
#                 print(mat[i][j],end=" ")
#             else:
#                 print("*",end=" ")
#         print()
# upperTri(mat)

# Print only the lower triangle and change all upper value to *
# def lowerTri(mat):
#     rows = len(mat)
#     cols = len(mat[0])
#     for i in range(0,rows):
#         for j in range(0,cols):
#             if j <= i:
#                 print(mat[i][j],end=" ")
#             else:
#                 print("*",end=" ")
#         print()
# lowerTri(mat)

# Print only the diagonal and change all value to *
# def diagonal1(mat):
#     rows = len(mat)
#     cols = len(mat[0])
#     for i in range(0,rows):
#         for j in range(0,cols):
#             if j == i:
#                 print(mat[i][j],end=" ")
#             else:
#                 print("*",end=" ")
#         print()
# diagonal1(mat)
# def diagonal2(mat):
#     rows = len(mat)
#     cols = len(mat[0])
#     for i in range(rows):
#         for j in range(cols):
#             if j == cols - i - 1:
#                 print(mat[i][j], end=" ")
#             else:
#                 print("*", end=" ")
#         print()
# diagonal2(mat)
# def bothDia(mat):
#     rows = len(mat)
#     cols = len(mat[0])
#     for i in range(rows):
#         for j in range(cols):
#             if j == cols - i - 1 or j ==i:
#                 print(mat[i][j], end=" ")
#             else:
#                 print("*", end=" ")
#         print()
# bothDia(mat)

#Transpose of matrix
def transpose(mat):
    rows = len(mat)
    cols = len(mat[0])
    result = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = mat[i][j]
    iterate(result)
transpose(mat)
