L = []
while True: 
    # Esse while não pode ser subtituido pelo for pois não há um vetor estabalecido
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    L.append(n)

for x in L:
    print(x)

