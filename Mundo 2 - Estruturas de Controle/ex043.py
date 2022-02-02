peso = int(input("Qual é o seu peso (Kg): "))
altura = float(input("Qual é a sua altura (m): "))

imc = peso / (altura ** 2)

print(f"O IMC dessa pessoa é de {imc:.1f}")

if (imc < 18.5):
    print("Você está ABAIXO do peso!")
elif (18.5 <= imc < 25):
    print("Você está no peso IDEAL!")
elif (25 <= imc < 30):
    print("Você está no SOBREPESO!")
elif (30 <= imc < 40):
    print("Você está na OBESIDADE!")
else:
    print("Você está na OBESIDADE MÓRBIDA!")

