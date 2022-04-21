divida_bruta = float(input('Qual é o valor da divida: '))
juros        = float(input('Qual é a taxa de juros:   '))
valor_mensal = float(input('Qual é o volar que será pago mensal: '))

juros      = juros / 100
valor_pago = 0

while (divida_bruta >= valor_pago):
    valor_pago = valor_pago + valor_mensal
    juros = valor_pago / divida_bruta


print(f'Sua divida inicial é de R$: {divida_bruta:5.2f}')
print(f'O valor a ser pago é de {valor_pago:5.2f}')
print(f'Com juros de {juros:3.2f}%')