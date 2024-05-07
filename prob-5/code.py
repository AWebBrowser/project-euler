primes=[]
def listPrimes(num): # want to list all primes from 1 to num.
    divisors=[]
    for i in range(num+1,2,-1):
        if (num%i)==0:
            divisors.append(i)
        for test in divisors:
            if primeTest(test):
                return test
    return divisors
def primeTest(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
listPrimes(30)
print(listPrimes(30))
