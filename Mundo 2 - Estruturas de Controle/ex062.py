print("Gerador de PA")
print("-=-" * 10)

a1 = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = a1
cont = 1
mais = 10
total_termos = 0

while mais != 0:
    total_termos += mais
    while (cont <= total_termos):
        #  total_termos += 1
        print(f"{termo}", end=' ')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
    #cont = 1  # zerando o contador
print(f"Progressão finalizada com {total_termos} termos mostrados.")
