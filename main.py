# estudando estruturas de controle de fluxo if, for e while

x = False

while not x:
    try:
        x = int(input("Digite um número inteiro: "))
        if x < 0:
            x = 0
            print('Número negativo.')
        elif x == 0:
            print('Zero.')
        elif x == 1:
            print('Um.')
        else:
            print('Mais que um.')
    except ValueError:
        print("Digite um valor válido.")
    