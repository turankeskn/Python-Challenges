

# Kata = https://www.codewars.com/kata/5526fc09a1bbd946250002dc


def find_outlier(integers):
    tek,cift,x,y=0,0,0,0
    for i in integers:
        if i%2==0:
            x=i
            cift+=1
        elif i%2!=0:
            tek+=1
            y=i
    return x if cift<tek else y