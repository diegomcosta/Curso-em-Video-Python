n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

op = maior = 0

while (op != 5):
    print("     [1] somar")
    print("     [2] multiplicar")
    print("     [3] maior")
    print("     [4] novos números")
    print("     [5] sair do programa")

    op = int(input(">>>>> Qual é a sua opção? "))
    if (op < 1 or op > 5):
        print("Opção inválida. Tente novamente")
    else:
        if (op == 1):
            print(f"A soma entre {n1} e {n2} é {n1 +n2}")
        elif (op == 2):
            print(f"O resultado de {n1} X {n2} é {n1 * n2}")
        elif (op == 3):
            maior = n1
            if (n2 > n1):
                maior = n2
            print(f"Entre {n1} e {n2} o maior valor é {maior}")
        elif (op == 4):
            print("Informe os números novamente:")
            n1 = int(input("Primeiro valor: "))
            n2 = int(input("Segundo valor: "))
        elif (op == 5):
            print("Finalizando...")
    print("=-=" * 10)
print("Fim do programa! Volte sempre!")