def count_common_unique(list1, list2):
    # list1: list of strings
    # list2: list of strings
    # return an integer
    d1=dict()
    d2=dict()
    for x in list1:
        if x in d1:
            d1[x]+=1
        else:
            d1[x]=1
    for y in list2:
        if y in d2:
            d2[y]+=1
        else:
            d2[y]=1
    s=set()
    for y in list2:
        if (y in d1) and (y in d2) and (d1[y]==1) and (d2[y]==1):
            s.add(y)
    count=len(s)
    del s
    return count