def maior_primo(x):
    i = 2
    num = 1
    if x >= 2:
        while num != 0:
            num = x % i
            i += 1
        i -= 1
        if i == x:
            print(x)
            return x
        x -= 1
        maior_primo(x)
    else:
        maior_primo(x)
