from random import choice
dados = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
jogadas = []


def LançarDados():
    lance = choice(dados)
    return lance


while True:
    play = input("Deseja jogar Craps? (Enter para sim e '0 + enter' para não)")
    if play == '0':
        break
    while True:
        jogada = LançarDados()
        jogadas.append(jogada)
        if jogadas[0] == 7:
            print("Você ganhou de primeira!!")
            print('------------')
            break
        elif jogadas[0] == 2 or jogadas[0] == 3 or jogadas[0] == 12:
            print("Craps. Você perdeu!!")
            print('------------')
            break
        else:
            while True:
                jogada = LançarDados()
                jogadas.append(jogada)
                aux = len(jogadas) - 2
                if jogada == jogadas[aux]:
                    print("Você ganhou, pois repetiu um valor sem ser 7.")
                    print('------------')
                    break
                if jogada == 7:
                    print("Você perdeu, tirou um 7.")
                    print('------------')
                    break
        break

