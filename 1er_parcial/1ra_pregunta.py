import numpy as np
import random

matriz = np.zeros((4, 4), int)
def cargar_matriz_aleatorios(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = random.randint(10, 100)

def mostrar_matriz(matriz):
    cadena = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            cadena += str(matriz[i][j]) +"  |  "
        print(cadena)
        cadena = ""

def contar_num_pares_debajo_diagonal(matriz):
    pares = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i>j:
                if matriz[i][j]%2 == 0:
                    pares +=1

    print(f"Cantidad de números pares de la parte inferior de la matriz: {pares}")

def promedio_diag(matriz):
    promedio = 0.0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i==j:
                promedio += matriz[i][j]
    promedio = promedio/4
    print(f"Promedio de los números que forman parte de la diagonal principal: {promedio}")

cargar_matriz_aleatorios(matriz)
mostrar_matriz(matriz)
contar_num_pares_debajo_diagonal(matriz)
promedio_diag(matriz)
