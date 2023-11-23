import random

cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 

def obtener_valor_carta(carta):
    return cartas[carta]

def barajar_cartas():
    return list(cartas.keys())

def jugar_blackjack():
    mazo = barajar_cartas()

    #jugador 2 cartas
    jugador_carta1 = random.choice(mazo)
    mazo.remove(jugador_carta1)
    jugador_carta2 = random.choice(mazo)
    mazo.remove(jugador_carta2)

    jugador_puntuacion = obtener_valor_carta(jugador_carta1) + obtener_valor_carta(jugador_carta2)

    print(f"Jugador: Carta 1: {jugador_carta1}, Carta 2: {jugador_carta2}], Puntuación: {jugador_puntuacion}")


    if jugador_puntuacion == 21:
        print("BLACKJACK. HAS GANADO")

    else:
    #crupier 2 cartas
        crupier_carta1 = random.choice(mazo)
        mazo.remove(crupier_carta1)
        crupier_carta2 = random.choice(mazo)

        crupier_puntuacion = obtener_valor_carta(crupier_carta1) + obtener_valor_carta(crupier_carta2)

        print(f"crupier: Carta 1: {crupier_carta1}, Carta 2: ?, Puntuación: {crupier_puntuacion}")




    #blackjack del crupier
    if crupier_puntuacion == 21:
        print("BLACKJACK CRUPIER. HAS PERDIDO")
    else:
    #  pedir cartas crupier
        while crupier_puntuacion < 17:
            nueva_carta = random.choice(mazo)
            crupier_puntuacion += obtener_valor_carta(nueva_carta)
      
            
        

    
    while True:
        tomar_carta = input("¿Pedir o plantarse? (p/pl): ").lower()
        if tomar_carta == 'p':
            nueva_carta = random.choice(mazo)
            mazo.remove(nueva_carta)
            jugador_puntuacion += obtener_valor_carta(nueva_carta)
            print(f"Jugador: Nueva carta [{nueva_carta}], Puntuación: {jugador_puntuacion}")

            if jugador_puntuacion > 21:
                print("Te has pasado de 21. HAS PERDIDO.")
                break
        elif tomar_carta == 'pl':
            
            if jugador_puntuacion == crupier_puntuacion:
                print("Has empatado con el crupier.")

            elif jugador_puntuacion > crupier_puntuacion:
                print("HAS GANADP")
            elif jugador_puntuacion < crupier_puntuacion:
                print("HAS PERDIDO")
            break
        else:
            print("Respuesta no válida. Por favor, ingresa 'p' para pedir o 'pl' para plantarte.")

if __name__ == "__main__":
    jugar_blackjack()