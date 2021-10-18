
# Kata = https://www.codewars.com/kata/586d6cefbcc21eed7a001155


def longest_repetition(chars):
    if not len(chars):
        return ('', 0)
    sum=1
    list=[]
    tup=()
    y=chars[0]
    n=1
    for i in range(len(chars)-1):
        if chars[i] == chars[i+1]:
            sum+=1
            if sum > n:
                n=sum
                y=chars[i]
        else:
            sum=1
    list.append(y)     
    list.append(n)
    tup=tuple(list)
    return tup      