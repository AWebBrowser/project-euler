# Goal: define a function with input n that iterates through all pythagorean triples until we have sum = 1000
# print(a*b*c).
#

def isPythTrip(a: int,b: int,c: int)-> bool:
    if (pow(a,2)+pow(b,2)== pow(c,2)):
        return True
    return False

def pythList(n: int,m: int)-> None:
    if m >n:
        a=pow(m,2)-pow(n,2)
        b=2*m*n
        c=pow(m,2)+pow(n,2)
        print("The pythagorean triple associated with (",n,",",m,") is (",a,",",b,",",c,")")
        print("Their sum is",a+b+c,".")
        print("Their product is", a*b*c,".")
    return None

pythList(5,20) # Note that this comes from the fact that 20 is the largest number s.t 5<20 and 2*25*20=1000

# Note that a+b+c should be 1000, which is also 2m^2 + 2mn.
