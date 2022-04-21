saldo = float(input('Qual é o saldo inicial: '))
juros = float(input('Qual é a taxa de juros: '))

juros = juros / 100

x = 1
while x <= 24:
    saldo = (saldo * juros) + saldo
    x = x + 1

print(f'No final de 24 meses o saldo será de R$: {saldo:5.2f}')