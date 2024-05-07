def diffSum(n):
    sumThenSquare=(sum(range(1,n+1)))**2
    sqSum=0
    for i in range(1,n+1):
        sqSum+=i**2
    print("Difference:",sumThenSquare - sqSum)
diffSum(100)
