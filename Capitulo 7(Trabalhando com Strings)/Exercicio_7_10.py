print("Tic tac toe\n")

JOGADOR1 = ' X '
JOGADOR2 = ' O '
linhas = [
    ['   ','|   |','   '], 
    ['---','+---+','---'],
    ['   ','|   |','   '],
    ['---','+---+','---'],
    ['   ','|   |','   '],
]

jogador = [JOGADOR1,JOGADOR2]
indice = 0
jogadas = []

while True:    
    
    print(f'Jogador {jogador[indice]}')

    for linha in linhas:
        for coluna in linha:
            print(f'{coluna}',end="")
        print()

    if (linhas[0][0] == JOGADOR1 or linhas[0][0] == JOGADOR2) and linhas[0][0] == linhas[0][1].strip("|") and linhas[0][0] == linhas[0][2]:
        print(f'O Jogador {linhas[0][0]} venceu')
        break

    if (linhas[0][0] == JOGADOR1 or linhas[0][0] == JOGADOR2) and linhas[0][0] == linhas[2][1].strip("|") and linhas[0][0] == linhas[4][2]:
        print(f'O Jogador {linhas[0][0]} venceu')
        break

    if (linhas[0][0] == JOGADOR1 or linhas[0][0] == JOGADOR2) and linhas[0][0] == linhas[2][0] and linhas[0][0] == linhas[4][0]:
        print(f'O Jogador {linhas[0][0]} venceu')
        break

    if (linhas[0][1].strip("|") == JOGADOR1 or linhas[0][1].strip("|") == JOGADOR2) and linhas[0][1] == linhas[2][1] and linhas[0][1] == linhas[4][1]:
        print(f'O Jogador {linhas[0][1].strip("|")} venceu')
        break

    if (linhas[0][2] == JOGADOR1 or linhas[0][2] == JOGADOR2) and linhas[0][2] == linhas[2][2] and linhas[0][2] == linhas[4][2]:
        print(f'O Jogador {linhas[0][2]} venceu')
        break

    if (linhas[0][2] == JOGADOR1 or linhas[0][2] == JOGADOR2) and linhas[0][2] == linhas[2][1] and linhas[0][2] == linhas[4][0]:
        print(f'O Jogador {linhas[0][2]} venceu')
        break

    if (linhas[2][0] == JOGADOR1 or linhas[2][0] == JOGADOR2) and  linhas[2][0] == linhas[2][1].strip("|") and linhas[2][0] == linhas[2][2]:
        print(f'O Jogador {linhas[2][0]} venceu')
        break
    
    if  (linhas[4][0] == JOGADOR1 or linhas[4][0] == JOGADOR2) and linhas[4][0] == linhas[4][1].strip("|") and linhas[4][0] == linhas[4][2]:
        print(f'O Jogador {linhas[4][0]} venceu')
        break

    if  (linhas[4][0] == JOGADOR1 or linhas[4][0] == JOGADOR2) and linhas[4][0] == linhas[2][1].strip("|") and linhas[4][0] == linhas[0][2]:
        print(f'O Jogador {linhas[4][0]} venceu')
        break
    
    if len(jogadas) == 9:
        print("\nEmpatou!!!")
        break

    campo = int(input('\nEscolha o campo: '))
    
    if campo in jogadas:
        print("\n\nCampo já foi escolhido, tente novamente:\n")
        continue

    if campo < 1 or campo > 9:
        print("\n\nCampo invalido\n")
        continue

    if campo == 1:
        linhas[0][0] = f'{jogador[indice]}'
    elif campo == 2:
        linhas[0][1] = f'|{jogador[indice]}|'
    elif campo == 3:
        linhas[0][2] = f'{jogador[indice]}'
    elif campo == 4:
        linhas[2][0] = f'{jogador[indice]}'
    elif campo == 5:
        linhas[2][1] = f'|{jogador[indice]}|'
    elif campo == 6:
        linhas[2][2] = f'{jogador[indice]}'
    elif campo == 7:
        linhas[4][0] = f'{jogador[indice]}'
    elif campo == 8:
        linhas[4][1] = f'|{jogador[indice]}|'
    elif campo == 9:
        linhas[4][2] = f'{jogador[indice]}'

    jogadas.append(campo)
    indice = abs(indice - 1)



