n = int(input("Digite um número para \ncalcular seu Fatorial: "))
print(f"calculando {n}! = ", end = "")
i = n
fat = 1
while (i > 0):
    print(i, end = "")
    print(" x " if i > 1 else " = ", end="")
    fat *= i
    i -= 1
print(f"{fat}")