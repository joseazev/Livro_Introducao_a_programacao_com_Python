L = [7,4,5,12,8]
fim = len(L)

while fim > 1:
    trocou = False
    x = 0
    while x < (fim -1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1

        if trocou:
            break

    fim -= 1
for e in L:
    print(e)

