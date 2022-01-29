from gettext import find


nome = str(input("Qual é o seu nome completo? ")).strip()
achado = "SILVA" in nome.upper()
print(f"Seu nome tem Silva? {achado}")