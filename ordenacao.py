#Ao digitar os valores, o codigo analisa se os valores estão em ordem crescente ou não

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a < b and b < c:
    print("crescente")
else:
    print("não está em ordem crescente")
