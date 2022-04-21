# valor acima de 200km 0.45 abaixo de 200km 0.50

distancia = float(input('Qual a distancia terá o trageto? '))

if (distancia < 200):
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

print(f'O valor a ser pago é {valor}')