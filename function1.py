# É o mesmo exercicio de fatorial, só que utiliza função
def fatorial(x):
    y = 1
    while x > 1:
        y = y * x
        x -= 1
    return(y)
    
x = int(input("Digite uma valor inteiro positive: "))

print("O valor fatorado é:", fatorial(x))