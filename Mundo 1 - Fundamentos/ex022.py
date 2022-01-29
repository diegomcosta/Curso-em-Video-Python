nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
nomeSemEspacos = nome.replace(" ", "")
print(f"Seu nome tem ao todo {len(nomeSemEspacos)} letras")
nomeDividido = nome.split()
primeiroNome = nomeDividido[0]
print(f"Seu primeiro nome é {primeiroNome} e ele tem {len(primeiroNome)} letras")
