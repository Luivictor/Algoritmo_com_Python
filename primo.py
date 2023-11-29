def primo(x):
    i = 2
    num = 1
    if x >= 2:
        while num != 0:
            num = x % i
            i += 1
        i -= 1
        if i == x:
            print("primo")
        else:
            print("nao primo")
    else:
        return x

x = int(input("Digite um valor maior que 1: "))
primo(x)