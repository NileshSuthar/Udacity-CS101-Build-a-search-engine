*one case failed*
def numbers_in_lists(string):
    # YOUR CODE
    result = []
    res = []
    flag = 0
    result.append(int(string[0]))
    for i in range(1,len(string)):
        if flag == 0:
            if int(string[i]) > result[-1]:
                result.append(int(string[i]))
            else:
                res.append(int(string[i]))
                flag = 1
                continue
        if flag == 1:
            k = res.pop()
            if int(string[i]) < k:
                res.append(k)
                res.append(int(string[i]))
                if(i == len(string)-1):
                    result.append(res)
            else:
                res.append(k)
                result.append(res)
                result.append(int(string[i]))
                flag = 0
                res = []
    return result
