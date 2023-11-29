def fatorial(x):
    y = 1
    while x > 1:
        y = y * x
        x -= 1
    return(y)
    
def binomial(n,k):
    return fatorial(n)/(fatorial(k) * fatorial(n - k))

    
n = int(input("Digite uma valor inteiro positive para N: "))
k = int(input("Digite uma valor inteiro positive para K: "))

print("O valor fatorado é:", binomial(n,k))