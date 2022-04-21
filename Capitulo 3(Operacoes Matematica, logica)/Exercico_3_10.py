# Exercício 3.10

# entradas
salario = float(input('Informe o valor do falario: '))
aumento = float(input('Informe o valor do aumento: '))

# calculos
aumento = aumento/100
reajuste = salario * aumento
salario = salario + reajuste


# saída
print(f'Com o reajuste de R${reajuste:5.2f}')
print(f'Novo salário será de R${salario:5.2f}')

