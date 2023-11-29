'''Ao digitar um valor qualquer, o codigo analisa se o 
valor em questão e divisivel por 3, caso seja, ele devol-
vera "Fizz", se não, devolvera o numero de entrada.'''

valor = int(input("Digite um valor para o teste: "))

if valor % 3 == 0:
    print("Fizz")
else:
    print(valor)