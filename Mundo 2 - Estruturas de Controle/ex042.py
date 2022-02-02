a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if (b - c < a < b + c) and (a - c < b < a + c) and (a - b < c < a + b):
    print("Os segmentos acima PODEM FORMAR um triângulo ", end="")
    if (a == b == c):
        print("EQUILÁTERO!")
    elif (a != b) and (a != c) and (b != c):
        print("ESCALENO!")
    elif (a == b != c) or (b == c != a) or (a == c != b):
        print("ISÓCELES!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")