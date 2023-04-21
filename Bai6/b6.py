a = int(input('a = '))
b = int(input('b = '))
print({i for i in range(1,a+b) if a%i==0 and b%i==0})