def split_string(source,splitlist):
    outp = []
    flag = True
    for i in source:
        if i in splitlist:
            flag = True
        else:
            if flag:
                outp.append(i)
                flag = False
            else:
                outp[-1] = outp[-1]+i
    return outp
