SUPERIOR = 0.1
INFERIOR = 0.15

salario = float(input('Informe o salario: '))

if (salario >= 1250):
    aumento = salario * SUPERIOR
    novo_salario = aumento + salario
else:
    aumento = salario * INFERIOR
    novo_salario = aumento + salario

print(f'O aumento será de R${aumento:5.2f}')
print(f'O novo salário será de R${novo_salario:5.2f}')
