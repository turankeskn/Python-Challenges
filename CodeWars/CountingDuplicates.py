

# Kata = https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/python



def duplicate_count(text):
    dict={}
    res=0
    for i in text:
        i=i.lower()
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=0
    for i in dict.values():
        if i > 0:
            res+=1
    return res