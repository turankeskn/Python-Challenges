

# Kata = https://www.codewars.com/kata/5e0b72d2d772160011133654



def solve(arr):
    arr.sort()
    result=arr[1]-arr[0]
    arr[2]-= result
    arr[1]-= result
    if arr[0] + arr[1] < arr[2]:
        return result + arr[0] + arr[1]
    else:
        half=arr[2]//2
        return result + half * 2 + arr[0]-half