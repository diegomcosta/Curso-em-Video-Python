print("Gerador de PA")
print("-=-" * 10)

a1 = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))
i = 1

while (i < 11):
    print(f"{a1 + (i-1)*r}", end=' ')
    i += 1
print("FIM")
