y = int(input("digite a largura: "))
x = int(input("digite a altura: "))

altura = 1
largura = 1
while altura <= x:
    while largura <= y:
        print("#", end = "")
        largura += 1
    altura += 1
    print()
    largura = 1