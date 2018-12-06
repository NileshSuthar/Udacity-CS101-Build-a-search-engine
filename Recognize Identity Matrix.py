def is_identity_matrix(matrix):
    #Write your code here
    count =0
    flag = 0
    for i in matrix:
        count +=1
    for i in matrix:
        if len(i) != count:
            flag = 1
            return False
    for i in range(count):
        for j in range(count):
            if i == j:
                if matrix[i][i] != 1:
                    flag = 1
                    return False
            else:
                if matrix[i][j] != 0:
                    flag = 1
                    return False
    if (flag == 0):
        return True

