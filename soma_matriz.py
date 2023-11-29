def dimensoes(matriz):
    return (len(matriz), len(matriz[0]))

def soma_matrizes(matriz1, matriz2):
    dimensaoMatriz1 = dimensoes(matriz1)
    dimensaoMatriz2 = dimensoes(matriz2)

    if dimensaoMatriz1 == dimensaoMatriz2:
        matrizSoma = []

        for i in range(len(matriz1)):
            linha = []

            for j in range(len(matriz1[0])):

                soma = matriz1[i][j] + matriz2[i][j]
                linha.append(soma)

            matrizSoma.append(linha)

        return matrizSoma
    else:
        return False