
# Kata = https://www.codewars.com/kata/54da5a58ea159efa38000836


def find_it(seq):
    for i in seq:
        result=0
        for j in seq:
            if i==j:
                result+=1     
        if result %2 !=0:
            return i