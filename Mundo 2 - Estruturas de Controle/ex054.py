from datetime import date
 
maioridade = menoridade = 0

for i in range (1, 8):
    anoNasc = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    idade = date.today().year - anoNasc
    if (idade < 18):
        menoridade += 1
    else:
        maioridade += 1

print(f"Ao todo tivemos {maioridade} pessoas maiores de idade")
print(f"E também tivemos {menoridade} pessoas menores de idade")
