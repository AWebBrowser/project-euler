def listPrimes(n):
    sum=0
    primes=[True for i in range(n+1)]
    p=2
    while (p*p)<=n:
        if (primes[p]==True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p+=1
    for p in range(2,n+1):
        if primes[p]:
            # check val print(p)
            sum+=p
    return sum


print("Result:",listPrimes(2_000_000))
print("Maximum Possible Ans (SANITY):",2000000*1999999//2)
