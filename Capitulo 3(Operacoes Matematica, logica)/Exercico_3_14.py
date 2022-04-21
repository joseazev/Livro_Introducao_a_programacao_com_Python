# Exercício 3.14

DIARIA = 60.0
VALOR_KILOMETRAGEM = 0.15

distancia = float(input('Quanto foi percorrido pelo carro? '))
dias = int(input('Quantos dias ficou com o carro? '))

total_diarias = dias * DIARIA
total_quilometragem = VALOR_KILOMETRAGEM * distancia

print(f'\nValor das diarias R${DIARIA:5.2f}: Total de dias {dias}')
print(f'Valor total das diarias R${total_diarias:5.2f}')
print('-' * 30)
print(f'\nValor por kilometro é de R${VALOR_KILOMETRAGEM}: Total de kilometragem {distancia}')
print(f'Valor total das diarias R${total_diarias:5.2f}')
print('=' * 30)
print(f'Total a pagar R${total_diarias + total_diarias:5.2f}')
