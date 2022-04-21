numero1 = int(input('Qual é o primeiro numero: '))
numero2 = int(input('Qual é o segundo numero: '))

print('''Qual é a operação:
    1 - soma
    2 - subtração
    3 - multiplicação
    4 - divisão
    ''')

operacao = int(input())

if (operacao == 1):
    print(numero1 + numero2)
elif (operacao == 2):
    print(numero1 - numero2)
elif (operacao == 3):
    print(numero1 * numero2)
elif (operacao == 4):
    print(numero1 / numero2)
else:
    print('Valor inválido!!')