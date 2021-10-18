
# Kata = https://www.codewars.com/kata/5ce399e0047a45001c853c2b





def parts_sums(ls):
    list=[0]
    toplam=0
    cıkartma=-1
    for i in range(len(ls)):
        toplam+=ls[cıkartma]
        list.append(toplam)
        cıkartma-=1
    list.reverse()
    return list