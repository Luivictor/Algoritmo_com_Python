valor = int(input("Digite o valor de n: "))
n = 1
i = 0

while valor >= 1:
    if valor == 0:
        print(n)
    else:
        n = n * (i + 1)
        i += 1
        valor -= 1
print(n)