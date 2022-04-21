soma = 0

while True:
    codigo     = int(input('Qual é o código do produto: '))
    if codigo == 0:
        break
    
    

    if codigo == 1:
        valor = 0.5
    elif codigo == 2:
        valor = 1
    elif codigo == 3:
        valor = 4 
    elif codigo == 5:
        valor = 7
    elif codigo == 9:
        valor = 8
    else:
        print('Código Inválido')
        continue
    
    quantidade = int(input('Informe a quantidade:       '))

    soma += (valor * quantidade)
    
print(f'Total a pagar: R$ {soma:5.2f}')
    