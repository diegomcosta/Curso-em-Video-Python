print("=" * 25)
print(" 10 TERMOS DE UMA PA")
print("=" * 25)

a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
a10 = a1 + 9 * r

for i in range(a1, a10+r , r):
    print(i, end=" - ")
print("Acabou")
