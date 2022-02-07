n = int(input("Digite um número: "))
divisores = 0
for i in range(1, n+1):
    if (n % i == 0):
        print("\033[34m" , end="")
        divisores += 1
    else:
        print("\033[31m", end="")
    print(f"{i}", end=" ")
print(f"\n\033[mO número {n} foi divisivel {divisores} vezes")
if (divisores == 2):
    print("E por isso ele É PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")