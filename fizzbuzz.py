'''Ao digitar um valor qualquer, o codigo analisa se o 
valor em questão e divisivel por 3 e 5, caso seja, ele devol-
vera "FizzBuzz", se não, devolvera o numero de entrada.'''

valor = int(input("Digite um valor para o teste: "))

if valor % 3 == 0 and valor % 5 == 0:
    print("FizzBuzz")
else:
    print(valor)