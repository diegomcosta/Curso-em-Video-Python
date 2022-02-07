frase = input("Digite uma frase: ").strip().upper()
frase = frase.replace(" ","")
inverso = frase[::-1]
print(f"O inverso de {frase} é {inverso}")
if (frase == inverso):
    print("A frase digitada é um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")