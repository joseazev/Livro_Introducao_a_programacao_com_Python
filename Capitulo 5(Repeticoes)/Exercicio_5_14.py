soma = 0
contador = 0

while True:
    
    numero = int(input('Digite um número (zero para sair): '))
    soma += numero

    if(numero == 0):
        break

    contador += 1

print(f'A soma dos numeros é {soma}')
print(f'A media dos numeros é {soma / contador:5.1f}')