l = [15, 7, 27, 39]
valores = input("Digite os valor a procurar: ")
valores = valores.split()

y = 0

while y < len(valores):
    x = 0

    while x < len(l):
        if l[x] == int(valores[y]):
            print(f"{valores[y]} acahado na posição {x}")
            break
        x += 1
    if x == len(l):
        print(f'{valores[y]} não encontrado')
    
    y += 1
