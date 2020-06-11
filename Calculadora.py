import os

while True:
    print("CALCULADORA")

    num1 = float(input("Digite o Primeiro numero: "))
    num2 = float(input("digite o Segundo numero: "))

    os.system("cls")

    print("1 _ Adicao")
    print("2 _ Subtracao")
    print("3 _ Divisao")
    print("4 _ Multiplicaçao")
    print("0 _ Sair")
    opcao = int(input("Digite a Opçao desejada: "))

    os.system("cls")

    if opcao == 1:
        print(num1, " + ", num2," = ", num1+num2)
        print("    ")
        cont = input("Deseja fazer outra operaçao? s/n:  ")
        if cont == 's':
            continue
        else:
            break
    elif opcao == 2:
        print(num1, " - ", num2, " = ", num1 - num2)
        print("    ")
        cont = input("Deseja fazer outra operaçao? s/n:  ")
        if cont == 's':
            continue
        else:
            break
    elif opcao == 3:
        print(num1, " / ", num2, " = ", num1 / num2)
        print("    ")
        cont = input("Deseja fazer outra operaçao? s/n:  ")
        if cont == 's':
            continue
        else:
            break
    elif opcao == 4:
        print(num1, " x ", num2, " = ", num1 * num2)
        print("    ")
        cont = input("Deseja fazer outra operaçao? s/n:  ")
        if cont == 's':
            continue
        else:
            break
    elif opcao == 0:
        os.system("cls")
        print("Saiu do Programa")
        break
    else:
        os.system("cls")
        print("Opçao Invalida!!")