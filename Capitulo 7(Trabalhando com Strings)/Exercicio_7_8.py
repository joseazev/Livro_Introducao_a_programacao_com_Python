palavras = ['uva','laranja', 'caqui', 'maca', 'melancia']

numero = int(input("digite o numero da sorte: "))
indice = (numero * 776) % len(palavras)

palavra = palavras[indice]

for x in range(100):
    print()

digitadas = []
acertos = []
erros = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "_"
    print(senha)
    if senha == palavra:
        print("Você acertou")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já digitou essa letra")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :  ")
    print("X  0  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "
    print(f"x{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 = " /   "
    elif erros >= 6:
        linha3 = " / \ "
    print(f"X{linha3}")

    if erros == 6:
        print("enforcado!")
        print(f"A palavra secreta é {palavra}")
        break


