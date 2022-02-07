c = s = media = idadeMaisVelho = nomeMaisVelho = menorDeVinte = 0

for i in range(1, 5):
    print("-" * 5, end=" ")
    print(f"{i}ª PESSOA",end=" ")
    print("-" * 5)

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper()
    if (sexo == "M"):
        if i == 1:
            idadeMaisVelho = idade
            nomeMaisVelho = nome
        else:
            if idade > idadeMaisVelho:
                idadeMaisVelho = idade
                nomeMaisVelho = nome
    elif (sexo == "F"):
        if (idade < 20):
            menorDeVinte += 1
    s += idade
    c += 1 
media = s / c

print()
print(f"A média de idade do grupo é de {media:.1f} anos")
print(f"O homem mais velho tem {idadeMaisVelho} anos e se chama {nomeMaisVelho}.")
print(f"Ao todo são {menorDeVinte} mulheres com menos de 20 anos")