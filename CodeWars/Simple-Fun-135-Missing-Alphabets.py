
# Kata = https://www.codewars.com/kata/58a664bb586e986c940001d5


def missing_alphabets(s):
    list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    fre={}
    sayi=1
    result=""
    for i in s:
        if i in fre:
            fre[i]+=1
            if fre[i]>sayi:
                sayi=fre[i]
        else:
            fre[i]=1
    for x in list:
        if x in fre:
            result+=(sayi-fre[x])*x
        else:
             result+=sayi*x
    return result       