# Leetcode - 74 : Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

#--------------------------Brute Force-------------------#
# def markInfinity(mat,row,col):
#     r,c = len(mat),len(mat[0])
#     for i in range(0,r):
#         mat[i][col] = float("Inf")
#     for j in range(0,c):
#         mat[row][j] = float("Inf")
# def setZeroes(mat):
#     r,c = len(mat),len(mat[0])
#     for i in range(0,r):
#         for j in range(0,c):
#             if mat[i][j] == 0:
#                 markInfinity(mat,i,j)
#     for i in range(0,r):
#         for j in range(0,c):
#             if mat[i][j] == float("Inf"):
#                 mat[i][j] = 0
#     return mat
# print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))

#-----------------------optimal-------------------------
def setZeroes(mat):
    r,c = len(mat),len(mat[0])
    rowTrack = [0 for _ in range(r)]
    colTrack = [0 for _ in range(c)]
    for i in range(0,r):
        for j in range(0,c):
            if mat[i][j] == 0:
                rowTrack[i] = -1
                colTrack[j] = -1
    for i in range(0,r):
        for j in range(0,c):
            if rowTrack[i] == -1 or colTrack[j] == -1:
                mat[i][j] = 0
    return mat
print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))   