def check(matrix , row , col , size_r , size_c):
    hang = []
    cot = []
    res = 0
    for i in range(row - 1 , row + 2):
        if i >= 0 and i < size_r:
            hang.append(i) 
    for i in range(col-1 , col+2):
        if i >= 0 and i < size_c:
            cot.append(i)
    for i in hang:
        for j in cot:
            if (i != row or j != col) and matrix[i][j]:
                res += 1
    return res

def minesweeper(matrix):
    res = [] # nen tao bien moi cho output
    size_r = len(matrix)
    size_c = len(matrix[0])
    for i in range(size_r):
        temp = []
        for j in range(size_c):
            temp.append(check(matrix , i , j , size_r , size_c))
        res.append(temp)
    return res


matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

print(minesweeper(matrix))