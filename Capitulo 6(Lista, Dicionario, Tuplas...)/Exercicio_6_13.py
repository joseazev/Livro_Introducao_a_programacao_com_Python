T = [-10, -8, 0, 1, 2, 5, -2, -4]
minimo = T[0]
maximo = T[0]

for x in T:
    if minimo > x:
        minimo = x
    
    if maximo < x:
        maximo = x
    
print(f'A temperatura minima é {minimo}, a temperatura máxima é {maximo}.')