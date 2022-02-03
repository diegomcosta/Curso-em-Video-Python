from random import choice
from time import sleep

vencedor = 0

print("Suas opções: ")
print("[ 1 ] PEDRA")
print("[ 2 ] PAPEL")
print("[ 3 ] TESOURA")

opcoes = ["Pedra", "Papel", "Tesoura"]
computador = choice(opcoes) 
jogador = int(input("Qual é a sua jogada? "))
print()

if (jogador == 1):
    jogador = "Pedra"
elif (jogador == 2):
    jogador = "Papel"
elif (jogador == 3):
    jogador = "Tesoura"

sleep(0.5)
print("JO", end="-")
sleep(1)
print("KEN", end="-")
sleep(1)
print("POOOO!\n")

if (jogador == computador):
    print("EMPATE!\n")
else:
    if( jogador == "Pedra"):
        if (computador == "Papel"):
            vencedor = "COMPUTADOR"
        elif (computador == "Tesoura"):
            vencedor = "JOGADOR"
    elif (jogador == "Papel"):
        if (computador == "Pedra"):
            vencedor = "JOGADOR"
        elif (computador == "Tesoura"):
            vencedor = "COMPUTADOR"
    elif (jogador == "Tesoura"):
        if (computador == "Papel"):
            vencedor = "JOGADOR"
        elif (computador == "Pedra"):
            vencedor == "COMPUTADOR"

    print(f'{vencedor} VENCEU\n')

print("-=" * 10)
print(f"Jogador jogou {jogador}.")
print(f"Computador jogou {computador}.")
print("-=" * 10)
print("\n")