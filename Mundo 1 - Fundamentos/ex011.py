l = float(input("Largura da parede: "))
h = float(input("Altura da parede: "))
area = l * h
print(f"Sua parede tem a dimensão de {l}X{h} e sua área é de {area:.3f}m².")
print(f"Para pintar essa parede, você precisará de {area/2:.4f}l de tinta.")