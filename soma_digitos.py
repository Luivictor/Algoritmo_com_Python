x = int(input("Digite um número inteiro: "))
a = 0 
b = 0

while x != 0:
    a = x % 10
    x = x // 10
    b = b + a
print(b)