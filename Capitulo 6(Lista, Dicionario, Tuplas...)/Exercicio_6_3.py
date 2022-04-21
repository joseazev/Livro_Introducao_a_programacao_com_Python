lista1 = [1,3,4,6]
lista2 = [1,3,4,5,7]
lista3 = lista1[:]
x = 0

while x < len(lista2):
    
    if lista2[x] not in lista3:
        lista3.append(lista2[x])
        continue
    
    x += 1

print(lista3)    
