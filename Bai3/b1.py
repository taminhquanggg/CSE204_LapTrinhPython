import math
def isPrime(n):
    for i in range (1, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n = int(input("N = "))
print("Là snt" if isPrime(n)==True else "Không là snt")