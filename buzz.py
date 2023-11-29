'''Ao digitar um valor qualquer, o codigo analisa se o 
valor em questão e divisivel por 5, caso seja, ele devol-
vera "Buzz", se não, devolvera o numero de entrada.'''

valor = int(input("Digite um valor para o teste: "))

if valor % 5 == 0:
    print("Buzz")
else:
    print(valor)