# Exercício 4.3 - Ler 3 numeros e informar qual é o maior e o menor numero.

numero1 = int(input('Entre com o primeiro número: '))
numero2 = int(input('Entre com o segundo número: '))
numero3 = int(input('Entre com o terceira número: '))

if (numero1 > numero2 and numero1 > numero3):
    print(f'O {numero1} é o maior número')

if (numero2 > numero1 and numero2 > numero3):
    print(f'O {numero2} é o maior número')

if (numero3 > numero1 and numero3 > numero2):
    print(f'O {numero3} é o maior número')


if (numero1 < numero2 and numero1 < numero3):
    print(f'O {numero1} é o menor número')

if (numero2 < numero1 and numero2 < numero3):
    print(f'O {numero2} é o menor número')

if (numero3 < numero1 and numero3 < numero2):
    print(f'O {numero3} é o menor número')
