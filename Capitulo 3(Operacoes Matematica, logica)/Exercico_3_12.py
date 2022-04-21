#Exercício 3.12

distancia = float(input('Qual a distancia da viagem?(KM) '))

velocidade_media = float(input('Qual a velocidade média pretendida?(km/h) '))

tempo_medio = distancia / velocidade_media

print(f'O caminho de {distancia}km com velocidade media de {velocidade_media}')
print(f'Será percorido em {tempo_medio} horas')
