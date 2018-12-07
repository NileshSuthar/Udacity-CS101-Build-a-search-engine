index = []
def add_to_index(index,keyword,url):
    flag = 0
    for i in index:
        if i[0] == keyword:
            i[1].append(url)
            flag = 1
    if flag == 0:
        res = []
        res.append(url)
        index.append([keyword,res])
        res = []
    return index
