#Exercício 3.9
SEGUNDOS_MINUTO = 3600    # segundos em minuto
SEGUNDOS_HORA   = 216000  # segundos em hora
SEGUNDOS_DIA    = 5184000 # segundos em dia

dia = int(input('Digite a quantide de dia: '))
segundos = dia * SEGUNDOS_DIA

horas = int(input('Digite a quantide de horas: '))
segundos += (horas * SEGUNDOS_HORA)

minutos = int(input('Digite a quantide de minutos: '))
segundos += (minutos * SEGUNDOS_MINUTO)

segundos += int(input('Digite a quantide de segundos: '))

print(f'São {segundos} segundos')
