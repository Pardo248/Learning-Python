import random

valor_minimo = 1
valor_maximo =6

juega_otra = "si"

while juega_otra == "si":
    print("El resultado es ...")
    print(random.randint(valor_minimo,valor_maximo))

    juega_otra = input("¿Quieres jugar otra vez?")


print("fin del juego")