import math
angulo = float(input("Digite o ângulo que você deseja: "))
#convertendo o angulo que esta em graus para radianos, pois as funções que utilizas graus trabalham com os mesmos em radianos
anguloRad = angulo * 0.01745 
# uma outra forma de converter o angulo é usando a função radians da biblioteca math

anguloNovo = math.radians(angulo)

seno = math.sin(anguloNovo)
coseno = math.cos(anguloRad)
tangente = math.tan(anguloRad)

print(f"O ângulo de {angulo:.1f} tem o SENO de {seno:.2f}")
print(f"O ângulo de {angulo:.1f} tem o COSENO de {coseno:.2f}")
print(f"O ângulo de {angulo:.1f} tem a TANGENTE de {tangente:.2f}")
