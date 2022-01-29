from random import randint
from time import sleep

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente advinhar...")
n = randint(0, 5)
x = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)
if (n != x):
    print(f"GANHEI! Eu pensei no número {n} e não no número {x}!")
else:
    print("PARABÉNS! Você conseguiu me vencer!")    
print("-=-" * 20)