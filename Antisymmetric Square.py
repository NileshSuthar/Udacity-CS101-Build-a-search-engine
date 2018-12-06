def antisymmetric(A):
    #Write your code here
    count = 0
    flag = 0
    for i in A:
        count += 1
    for i in range(count):
        for j in range(1,count):
            if i != j:
                if A[i][j] != -A[j][i]:
                    flag = 1
                    return False
    if(flag == 0):
        return True
