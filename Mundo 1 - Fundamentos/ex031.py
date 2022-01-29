d = float(input("Qual é a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {d:.1f}km.")
if (d <= 200):
    preco = 0.5 * d
else:
    preco = 0.45 * d
print(f"E o preço da sua passagem será de R${preco:.2f}")
