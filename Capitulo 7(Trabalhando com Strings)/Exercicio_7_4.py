s = 'TTAAC'
ultima_letra = ''
for letra in s:
    if ultima_letra == letra:
        continue
    
    ultima_letra = letra
    print(f'{letra}: {s.count(letra)}x')

