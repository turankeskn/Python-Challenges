
# Kata = https://www.codewars.com/kata/5287e858c6b5a9678200083c/python



def narcissistic( value ):
    value=str(value)
    sonuc=0
    for i in value:
        sonuc+=int(i)**len(value)
    if sonuc==int(value):
        print("value"+" is narcissistic")
        return True
    else:
        print("value"+" is not narcissistic")
        return False    