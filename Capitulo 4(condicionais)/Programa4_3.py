# Progama 4.3 - calculo de imposto de renda

salario = float(input('digite o salário para cáculo do imposto: '))
base = salario
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000

if base> 1000:
    imposto = imposto + ((base - 1000) * 0.2)

print(f'Salário: R${salario:6.2f} Imposto a pagar : R${imposto:6.2f}')

