ultimo = 10
fila1 = list(range(1, ultimo + 1))
fila2 = list(range(1, ultimo + 1))
parar = False

while True:
    print(f'\nexistem {len(fila1)} clientes na fila1')
    print(f'Fila A atual: {fila1}')
    print(f'\nexistem {len(fila2)} clientes na fila1')
    print(f'Fila B atual: {fila2}')
    
    escolha = input(f'Qual fila será atendida? (A ou B)')
    
    if escolha == 'A':
        fila = fila1
    elif escolha == 'B':
        fila = fila2
    else:
        print(f'Escolha A ou B.')
        continue

    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair')

    operacao = input("Operação (F, A ou S): ")

    for operador in operacao:

        if operador == 'A' or operador == 'a':
            if len(fila) > 0:
                atendimento = fila.pop(0)
                print(f'Cliente {atendimento} atendido')
            else:
                print('Fila vazia! Ninguém para atender.')
            
        elif operador == 'F' or operador == 'f':
            ultimo += 1
            fila.append(ultimo)
        
        elif operador == 'S' or operador == 's':
            parar = True
        else:
            print("Operação invalido! Digite apenas F, A ou S!")
        
    if parar:
        break