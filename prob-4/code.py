# Project Euler Problem #4: Largest Palindrome Product.
# Description: A palindromic number reads the same both ways. The largest palindrome made from two two-digit numbers is 9009=91x99
# Goal: Find the largest palindromic number made from three three-digit numbers.

# First Solution: Algorithm Runtime: O(n^2)

def is_palindrome(num): # Creates checker to see if the input is a palindrome.
    toCheck = str(num)  # Converts input into string, which is nicer to work with.
    if toCheck[::-1] == toCheck:
        return True
    else: 
        return False

def iterator(n,m):
    bigPal=0
    for i in range(n,m):
        for j in range(n,m):
            toCheck=i*j
            if is_palindrome(toCheck):
                if bigPal < toCheck:
                    bigPal=toCheck
                    print(toCheck)
    return bigPal

print(iterator(100,1000)) # prints all possible solutions in order: choose the largest one as answer.

# Profile time on Apple M2 MBP: 199ms
