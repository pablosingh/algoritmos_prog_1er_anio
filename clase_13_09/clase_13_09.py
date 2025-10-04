import numpy as np

def hayGanador(matriz, cantidad):
    respuesta = (
            ganadorFila(matriz, cantidad) or
            ganadorDiagonalPrincipal(matriz, cantidad) or
            ganadorDiagonalSecundaria(matriz, cantidad) or
            ganadorColumna(matriz, cantidad)
                 )
    return respuesta

def ganadorFila(matriz, cantidad):
    bandera = False
    continuos = 0
    for i in range(0, cantidad - 1, 1):
        for j in range(0, cantidad - 1, 1):
                if (matriz[i][j] == matriz[i][j + 1]) and matriz[i][j] != 0.0 :
                    continuos += 1
        if continuos == cantidad-1:
            bandera = True
            break
        continuos = 0
    #print(f"continuos : {continuos}")
    #print(f"bandera fila : {bandera}")
    return bandera

def ganadorColumna(matriz, cantidad):
    bandera = False
    continuos = 0
    for i in range(0, cantidad - 1, 1):
        for j in range(0, cantidad - 1, 1):
            if (matriz[i][j] == matriz[i+1][j]) and matriz[i][j] != 0.0 :
                continuos += 1
        if continuos == cantidad-1:
            bandera = True
            break
        continuos = 0
    #print(f"continuos : {continuos}")
    #print(f"bandera columna : {bandera}")
    return bandera

def ganadorDiagonalPrincipal(matriz, cantidad):
    bandera = True
    continuos = 0
    for i in range(0, cantidad-1, 1):
        for j in range(0, cantidad-1, 1):
            if i == j:
                if (matriz[i][j] == matriz[i + 1][j + 1]) and matriz[i][j] != 0.0:
                    continuos += 1
                else:
                    bandera = False
                    #print(f"bandera diag principal : {bandera}")
                    return bandera
    #print(f"bandera diag principal : {bandera}")
    return bandera

def ganadorDiagonalSecundaria(matriz, cantidad):
    bandera = True
    continuos = 0
    for i in range(0, cantidad-1, 1):
        for j in range(0, cantidad-1, 1):
            if i+j == cantidad-1:
                if (matriz[i][j] == matriz[i + 1][j + 1])and matriz[i][j] != 0.0:
                    continuos += 1
                else:
                    bandera = False
                    #print(f"bandera diag secundaria : {bandera}")
                    return bandera
    #print(f"bandera diag secundaria : {bandera}")
    return bandera

def estaLleno(matriz, cantidad):
    bandera = True
    for i in range(0, cantidad, 1):
        for j in range(0, cantidad, 1):
            if matriz[i][j] == 0:
                bandera = False
                return bandera
    return bandera

def mostrar(matriz, cantidad):
    #print(matriz)
    for i in range(0, cantidad, 1):
        cadena = ""
        cadenaGuiones = ""
        for j in range(0, cantidad, 1):
            if matriz[i][j] == 1:
                cadena = cadena + "X "
            elif matriz[i][j] == 2:
                cadena = cadena + "O "
            else:
                cadena = cadena + "# "
            cadenaGuiones = cadenaGuiones + "--"
        print(cadena)
        #print(cadenaGuiones)

def jugar(matriz, cantidad, jug):
    while True:
        if jug == True:
            print("juega X")
        else:
            print("juega 0")
        fila = int(input("Fila : "))
        columna = int(input("Columna : "))
        if (fila>cantidad) or (columna>cantidad):
            print("Fuera de rango")
            continue
        if matriz[fila-1][columna-1] != 0:
            print("posicion ocupada")
            continue
        if jug:
            matriz[fila-1][columna-1] = 1
        else:
            matriz[fila-1][columna-1] = 2
        break

def mi_main():
    cantidad = int(input("Ingrese la cantidad de filas/col : "))
    matriz = np.zeros([cantidad, cantidad])

    jug1 = True
    tableroLleno = False
    ganador = False

    while not (tableroLleno or ganador):
        jugar(matriz, cantidad, jug1)
        mostrar(matriz, cantidad)
        tableroLleno = estaLleno(matriz, cantidad)
        ganador = hayGanador(matriz, cantidad)
        if ganador:
            print("Felicidades!")
            if jug1:
                print("Jugador 1 has ganado")
            else:
                print("Jugador 2 has ganado")
        jug1 = not jug1
    if tableroLleno: print("Tablero lleno")
    print("Fin")
mi_main()