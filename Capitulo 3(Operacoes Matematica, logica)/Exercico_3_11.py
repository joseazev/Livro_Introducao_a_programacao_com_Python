#Exercicio 3.11

valor = float(input('Entre com o valor: '))
desconto = float(input('Entre com o desconto: '))

desconto = desconto / 100

valor_desconto = valor * desconto

print(f'Desconto de R${valor_desconto:5.2f}')
print(f'Valor final R${valor - valor_desconto:5.2f}')

