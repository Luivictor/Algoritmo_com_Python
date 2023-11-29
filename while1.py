numerico = int(input("Digite um número inteiro: "))
a = 0 
b = 0
c = 0
resultado = 0

while numerico >= 9:
    if numerico >= 1000:
        a = numerico // 1000
        numerico = numerico % 1000
    elif numerico >= 100:
        b = numerico // 100
        numerico = numerico % 100
    else:
        c = numerico // 10
        numerico = numerico % 10
        
resultado = b + a + c + numerico
print(resultado)