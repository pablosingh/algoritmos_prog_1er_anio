import numpy as np

def hayGanador(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    bandera = True
    for i in range(0, filas, 1):
        for j in range(0, columnas, 1):
            if matriz[i][j] == 0:
                bandera = False
                return bandera
    return bandera

def ganadorFila(matriz, cantidad):
    jugador = 0.0
    bandera = True
    continuos = 0
    for i in range(0, cantidad - 1, 1):
        for j in range(0, cantidad - 1, 1):
            if i + j == cantidad - 1:
                if matriz[i][j] == matriz[i + 1][j + 1]:
                    continuos += 1
                    jugador = matriz[i][j]
                else:
                    return False, jugador
    return bandera, jugador

def ganadorDiagonalSecundaria(matriz, cantidad):
    jugador = 0.0
    bandera = True
    continuos = 0
    for i in range(0, cantidad-1, 1):
        for j in range(0, cantidad-1, 1):
            if i+j == cantidad-1:
                if matriz[i][j] == matriz[i + 1][j + 1]:
                    continuos += 1
                    jugador = matriz[i][j]
                else:
                    return False , jugador
    return bandera, jugador

def ganadorDiagonalPrincipal(matriz, cantidad):
    jugador = 0.0
    bandera = True
    continuos = 0
    for i in range(0, cantidad-1, 1):
        for j in range(0, cantidad-1, 1):
            if i == j:
                if matriz[i][j] == matriz[i + 1][j + 1]:
                    continuos += 1
                    jugador = matriz[i][j]
                else:
                    return False , jugador
    return bandera, jugador

def estaLleno(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    bandera = True
    for i in range(0, filas, 1):
        for j in range(0, columnas, 1):
            if matriz[i][j] == 0:
                bandera = False
                return bandera
    return bandera

def mostrar(matriz, cantidad):
    print(matriz)
    for i in range(0, cantidad, 1):
        cadena = ""
        for j in range(0, cantidad, 1):
            if matriz[i][j] == 1:
                cadena = cadena + "x "
            elif matriz[i][j] == 2:
                cadena = cadena + "o "
            else:
                cadena = cadena + "# "
        print(cadena)


def jugar(matriz, jug):
    fila = int(input("Fila : "))
    columna = int(input("Columna : "))
    if jug:
        matriz[fila][columna] = 1
    else:
        matriz[fila][columna] = 2

def mi_main():
    cantidad = int(input("Ingrese la cantidad de filas/col : "))
    matriz = np.zeros([cantidad, cantidad])

    jug1 = True
    tableroLleno = False
    ganador = False

    while not tableroLleno:
        jugar(matriz, jug1)
        mostrar(matriz, cantidad)
        tableroLleno = estaLleno(matriz)
        jug1 = not jug1
    print(f"Fin : {tableroLleno}")
mi_main()