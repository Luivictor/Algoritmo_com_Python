#Ao digitar um valor qualquer, o programa busca o numero Primo mais proximo

def maior_primo(x):
    i = 2
    num = 1
    if x >= 2:
        while num != 0:
            num = x % i
            i += 1
        i -= 1
        if i == x:
            return(x)
        else:
            x -= 1
            return maior_primo(x)
    return(x)

x = int(input("Digite um valor maior que 1: "))
print(maior_primo(x))