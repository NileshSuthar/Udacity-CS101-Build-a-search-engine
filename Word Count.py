def count_words(sd):
    count = 0
    if len(sd) == 0:
        return count 
    else:
        for i in range(len(sd)):
            if sd[i] == " ":
                count+=1
    return count+1
