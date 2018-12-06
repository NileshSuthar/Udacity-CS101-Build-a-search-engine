def symmetric(lis):
    # Your code here
    n=0
    flag =0
    for i in lis:
        n += 1
    for i in lis:
        if len(i) != n:
            flag = 1
            return False
    for i in range(n):
        for j in range(n):
            if lis[i][j] != lis[j][i]:
                flag=1
                return False
            else:
                continue
    if flag == 0:
        return True 
