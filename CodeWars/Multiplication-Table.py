
# Kata = https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08


def multiplication_table(size):
    result=[]
    for i in range(1,size+1):
        list=[]
        for x in range(1,size+1):
            list.append(i*x)
        result.append(list)
    return result