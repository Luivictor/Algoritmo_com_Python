# É o mesmo exercicio de function1, só que desta vez o programa chama a função soma que faz a adição entre os valores de fatorial(x)
def fatorial(x):
    y = 1
    while x > 1:
        y = y * x
        x -= 1
    return(y)
    
def soma():
    return fatorial(x) + fatorial(x)
    
x = int(input("Digite uma valor inteiro positive: "))

print("O valor fatorado é:", soma())