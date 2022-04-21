dividendo = int(input('Digite o primeiro numero: '))
divisor   = int(input('Digite o segundo numero:  '))
resultado = 0
diferenca = 0
resto = 0
while resultado >= divisor:
    resto = divisor - resultado
    if resto < divisor:
        diferenca = resto
    

print(resto)
print(diferenca)