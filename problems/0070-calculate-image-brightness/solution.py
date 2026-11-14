
def calculate_brightness(img):
    # Write your code here
    if img==[]:
        return -1
    total_brightness=0
    k=len(img[0])
    for x in img:
        if len(x)!=k:
            return -1
        for y in x:
            if y is None:
                return -1
            if y<0 or y>255:
                return -1
            total_brightness+=y
    return total_brightness/(len(img)*len(img[0]))
