def biggest(a,b,c):
    def big(a,b):
        if(a>b):
            return a
        if(a<b):
            return b
        if(a==b):
            return a
    return big(big(a,b),c)
