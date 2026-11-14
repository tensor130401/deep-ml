def add_two_numbers(l1, l2):
    # l1 and l2 are lists of digits in reverse order
    ans=[]
    carry=0
    x=len(l1)
    y=len(l2)
    i=0
    j=0
    while i<x and j<y:
        k=l1[i]+l2[j]
        if carry:
            k+=1
            carry=0
        if k>=10:
            carry=1
            k=k%10
        ans.append(k)
        i+=1
        j+=1
    while i<x:
        k=l1[i]
        if carry:
            k+=1
            carry=0
        if k>=10:
            carry=1
            k=k%10
        ans.append(k)
        i+=1
    while j<y:
        k=l2[j]
        if carry:
            k+=1
            carry=0
        if k>=10:
            carry=1
            k=k%10
        ans.append(k)
        j+=1
    if carry:
        ans.append(carry)
    return ans
    pass