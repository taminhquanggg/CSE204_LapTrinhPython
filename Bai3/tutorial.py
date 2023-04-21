# #B1
# def isPrime(n):
#     i = 2
#     if n < 2:
#         return False
#     while i<=int(n**0.5):
#          if n % i == 0:
#              return False
#          else:
#              i = i + 1
#     return True
# n = int(input('n = '))
# print(isPrime(n))

# #b2
# def isPrime(n):
#     i = 2
#     if n < 2:
#         return False
#     while i<=int(n**0.5):
#          if n % i == 0:
#              return False
#          else:
#              i = i + 1
#     return True
# a = int(input('A = '))
# b = int(input('B = '))
# for i in range(a, b):
#     if isPrime(i):
#         print(i, end=' ')

# #b3
# def UCLN(a, b):
#     while a*b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     return a + b
# def BCNN(a, b):
#     return (a * b) / UCLN(a, b)
# a = int(input('a = '))
# b = int(input('b = '))
# print('UCLN =',UCLN(a,b),'BCNN =',int(BCNN(a,b)))

# #b4
# while True:
#     n = int(input())
#     if n < 0:
#         break

# #b5
# def UCLN(a, b):
#     while a*b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     return a + b
# def BCNN(a, b):
#     return (a * b) / UCLN(a, b)
# a, b = 0, 1
# ucln = 0
# bcnn = 1
# while True:
#     n = int(input())
#     if n<=0:
#         break
#     ucln = UCLN(ucln, n)
#     bcnn = BCNN(bcnn, n)
#
# print('UCLN =', ucln, 'BCNN = ', int(bcnn))

#b6
def fibo(n, k):
    if n<0:
        return 0
    if n<k:
        return n
    s = 0
    for i in range(k, 0, -1):
        s = s + fibo(n - i - 1, k)
    return s
