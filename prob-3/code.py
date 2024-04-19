def prime(n):
    primes=[]
    uppBound = int(n**(0.5))
    for i in range(uppBound+1,2,-1):
        if (n%i) ==0:
            primes.append(i)
    print(primes)
    for num in primes:
        if primeTest(num):
            return num 
    return primes

def primeTest(n):
    if n%2==0 or n%5==0:
        return False
    for i in range(3,n//2,2):
        if n%i==0:
            return False
    return True

print(prime(600851475143))
