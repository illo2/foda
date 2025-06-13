# esta versión es la base para trabajar en la evaluación III
def crear_tablero():
    tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    return tablero

def imprimir_tablero(tablero):
        print(f"{tablero[0][0]}|{tablero[0][1]}|{tablero[0][2]}")
        print("-----")
        print(f"{tablero[1][0]}|{tablero[1][1]}|{tablero[1][2]}")
        print("-----")
        print(f"{tablero[2][0]}|{tablero[2][1]}|{tablero[2][2]}")

def movimiento_jugador(tablero, jugador):
    while True:
        try:
            fila = int(input("Elige fila (0, 1, 2): "))
            columna = int(input("Elige columna (0, 1, 2): "))
            if 0 <= fila <= 2 and 0 <= columna <= 2:
                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador
                    break
                else:
                    print("¡Casilla ocupada!")
            else:
                print("¡Entrada inválida! Por favor, elige fila y columna entre 0, 1 y 2.")
        except ValueError:
            print("¡Entrada inválida! Por favor, ingresa números.")


def hay_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True

    return False

def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

import random

def minimax(tablero, profundidad, is_maximizing):
    if hay_ganador(tablero):
        return 1 if not is_maximizing else -1
    if tablero_lleno(tablero):
        return 0

    if is_maximizing:
        mejor_puntuacion = -float('inf')
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == " ":
                    tablero[i][j] = "O"
                    puntuacion = minimax(tablero, profundidad + 1, False)
                    tablero[i][j] = " "  # Deshacer movimiento
                    mejor_puntuacion = max(mejor_puntuacion, puntuacion)
        return mejor_puntuacion
    else:
        mejor_puntuacion = float('inf')
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == " ":
                    tablero[i][j] = "X"
                    puntuacion = minimax(tablero, profundidad + 1, True)
                    tablero[i][j] = " "  # Deshacer movimiento
                    mejor_puntuacion = min(mejor_puntuacion, puntuacion)
        return mejor_puntuacion


def movimiento_ia(tablero):
    mejor_puntuacion = -float('inf')
    mejor_movimiento = None
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                tablero[i][j] = "O"
                puntuacion = minimax(tablero, 0, False)
                tablero[i][j] = " "  # Deshacer movimiento
                if puntuacion > mejor_puntuacion:
                    mejor_puntuacion = puntuacion
                    mejor_movimiento = (i, j)

    if mejor_movimiento:
        tablero[mejor_movimiento[0]][mejor_movimiento[1]] = "O"

def juego_completo():
    victorias_X = 0
    victorias_O = 0
    empates = 0

    while True:
        tablero = crear_tablero()
        jugador_actual = "X"

        while True:
            imprimir_tablero(tablero)
            print(f"Turno de {jugador_actual}")
            if jugador_actual == "X":
                movimiento_jugador(tablero, jugador_actual)
            else:
                movimiento_ia(tablero)

            if hay_ganador(tablero):
                imprimir_tablero(tablero)
                print(f"¡{jugador_actual} ha ganado!")
                if jugador_actual == "X":
                    victorias_X += 1
                else:
                    victorias_O += 1
                break

            if tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print("¡Empate!")
                empates += 1
                break

            if(jugador_actual=="O"):
                jugador_actual="X"
            else:
                jugador_actual = "O"

        print(f"Victorias X: {victorias_X}")
        print(f"Victorias O: {victorias_O}")
        print(f"Empates: {empates}")

        jugar_de_nuevo = input("¿Deseas jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            break

juego_completo()
