L = [7, 2, 1, 8]
minimo = L[0]
for x in L:
    if minimo > x:
        minimo = x
    
print(f'O menor numero da lista é {minimo}')