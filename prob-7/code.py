import math 

def primeTest(n):
    if n%2==0 or n%3==0:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True

def check(m):
    possibleNumbers=[]
    primeArray = [];

    for k in range(0,int((3/2)*(m+1)*math.log(m+1))): # 
        possibleNumbers.append(k)
    for i in possibleNumbers:
        if primeTest(i):
            primeArray.append(i);
    print(primeArray[m-2])
    return

check(10001)
