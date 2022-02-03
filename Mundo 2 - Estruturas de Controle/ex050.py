s = c = 0
for i in range(1, 7):
    x = int(input(f"Digite o {i}o valor: "))
    if (x % 2 == 0):
        s += x
        c += 1
print(f"A soma dos {c} números pares vale {s}")