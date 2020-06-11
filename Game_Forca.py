import os


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


def trocarchar(indices, nchar="", pala=""):
    lista = []
    for letra in pala:
        lista.append(letra)
    for iden in indices:
        lista[int(iden)] = nchar
    mudchar = ""
    for tempchar in lista:
        mudchar += tempchar
    return mudchar


print("JOGO DA FORCA")
while True:
    chances = 3
    plvused = ""
    plcurrent = ""
    palavra = str(input("Digite a Palavra: "))
    dica = str(input("Digite um dica: "))

    os.system("cls")

    qtletra = len(palavra)
    for it in range(qtletra):
        plcurrent += "_"

    while True:
        print("Chances:", chances)
        print("Dica:", dica)
        print("palavras usadas:", plvused)

        for curen in plcurrent:
            print(curen)

        while True:
            print("")
            currletra = str(input("Digite uma letra:"))
            if currletra in plvused:
                print("ja foi usada essa letra!")
            else:
                break

        if currletra in palavra:
            plvused += currletra
            plcurrent = trocarchar(list(find_all(palavra, currletra)), currletra, plcurrent)
            if plcurrent == palavra:
                os.system("cls")
                print("Chances:", chances)
                print("Dica:", dica)
                print("palavras usadas:", plvused)

                for curen in plcurrent:
                    print(curen)
                print("Parabens. Voce Descobriu a Palavra: ", palavra)
                break
        else:
            chances -= 1
            plvused += currletra
            if chances == 0:
                print("Voce Perdeu")
                break
        os.system("cls")

    dnv = str(input("Jogar Novamente (s / n): "))
    print(dnv)
    if not dnv.find("s") != 0:
        os.system("cls")
    else:
        break

os.system("cls")
print("Fim de game")
