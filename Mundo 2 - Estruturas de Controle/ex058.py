from random import randint

tentativa = 1

print("Sou seu computador...")
print("Acabei de pensar em um número entre 0 e 10.")
computador = randint(0, 10)
print("Será que voce consegue adivinhar qual foi?")
jogador = int(input("Qual é o seu palpite? "))

while (jogador != computador):
    tentativa += 1
    if (jogador > computador):
        print("Menos... Tente mais uma vez.")
    else:
        print("Mais... Tente mais uma vez.")
    jogador = int(input("Qual é o seu palpite? "))
print(f"Acertou com {tentativa} tentativa(s). Parabéns!")