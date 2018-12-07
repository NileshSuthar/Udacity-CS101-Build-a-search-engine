index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    res = content.split()
    flag = 0
    for i in res:
        for j in index:
            if i == j[0]:
                i[1].append(url)
                flag = 1
        if(flag == 0):
            index.append([i,[url]])
    return index
