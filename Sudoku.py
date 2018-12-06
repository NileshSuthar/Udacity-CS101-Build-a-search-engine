def check_sudoku(lis):
    n = 0
    flag = 0
    for i in lis:
        n += 1
    for i in lis:
        for j in range(1,n+1):
            if j not in i:
                flag = 1
                return False
            else:
                continue
    for i in range(n):
        for j in range(1,n):
            if lis[0][i] == lis[j][i]:
                flag = 1
                return False
            else:
                continue
    if(flag == 0):
        return True
    
