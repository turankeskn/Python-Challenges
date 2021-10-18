
# Kata = https://www.codewars.com/kata/52998bf8caa22d98b800003a/solutions/python


def manhattan_distance(pointA, pointB):
    a=0
    for i in range(len(pointA)):
        a+=abs(pointA[i]-pointB[i])
    return a