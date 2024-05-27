def gerarMatrizIdentidade(size):
    identidade = [[0 for x in range(size)] for y in range(size)]

    for row in range(size):
        for col in range(size):
            if row == col:
                identidade[row][col] = 1
            else:
                identidade[row][col] = 0

    return identidade

def gerarMatrizExtendida(matrizOriginal, identidade):
    matrizExtendida = []
    for i in range(len(matrizOriginal)):
        matrizExtendida.append(matrizOriginal[i] + identidade[i])

    return matrizExtendida


def matrizInversa(matrizOriginal):
    size = len(matrizOriginal)
    identidade = gerarMatrizIdentidade(size)
    matrizExtendida = gerarMatrizExtendida(matrizOriginal, identidade)

    for i in range(size):
        pivot = matrizExtendida[i][i]

        for j in range(size*2):
            matrizExtendida[i][j] /= pivot

        for k in range(size):
            if k != i:
                fator = matrizExtendida[k][i]
                for j in range(size*2):
                    matrizExtendida[k][j] -= fator * matrizExtendida[i][j]

    inversa = [linha[size:] for linha in matrizExtendida]

    return inversa

matriz_original = [
        [1, 2, 3],
        [0, 1, 0],
        [1, 0, 2]
    ]

matriz_inversa = matrizInversa(matriz_original)
for linha in matriz_inversa:
    print(linha)