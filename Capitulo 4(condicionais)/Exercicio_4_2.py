MULTA_POR_KM = 5

velocidade =  int(input('Qual é a velocidade do carro: '))

if velocidade > 80:
    print('Você acaba de ser multado.')
    multa = (velocidade - 80) * MULTA_POR_KM
    print(f'O valor da sua multa é de R${multa:5.2f}')

