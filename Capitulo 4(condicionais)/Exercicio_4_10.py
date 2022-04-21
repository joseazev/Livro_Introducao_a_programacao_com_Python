instalacao = input('''
            Qual é o tipo de instação 
            r - residencial
            c - Comercial
            i - industrial

            ''')

consumo = float(input('Registre o consumo: '))

if(instalacao == 'r'):
    if consumo > 500:
        valor = consumo * 0.65
    else:
        valor = consumo * 0.4

if(instalacao == 'c'):
    if consumo > 1000:
        valor = consumo * 0.6
    else:
        valor = consumo * 0.55

if(instalacao == 'i'):
    if consumo > 5000:
        valor = consumo * 0.6
    else:
        valor = consumo * 0.55

print(valor)