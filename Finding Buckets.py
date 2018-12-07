def hashtable_get_bucket(htable,keyword):
    flag = 0
    for i in htable:
        for j in i:
            if j[0] == keyword:
                flag = 1
                return i
    if(flag == 0):
        return []
