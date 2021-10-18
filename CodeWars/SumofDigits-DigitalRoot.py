
# Kata = https://www.codewars.com/kata/541c8630095125aba6000c00


def digital_root(n): 
    while int(n) > 9:
        n=str(n)
        toplam=0
        for i in n:
            toplam+=int(i)
        n=toplam
    return n