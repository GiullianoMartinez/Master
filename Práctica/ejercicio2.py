"""
2. FRAGMENTOS DE ENERGÍA

Un guerrero tiene una lista de fragmentos de energía, representados como números enteros. Los fragmentos impares son inestables y deben eliminarse. El programa debe:

Leer una lista de números enteros.

Eliminar todos los números impares.

Calcular la suma total de los fragmentos restantes.

Ejemplo:

Entrada: [10, 5, 3, 8, 2, 7]
Salida: 20
(Porque 10 + 8 + 2 = 20)

"""
def poblar():
    lista = []
    while True:
        x = int(input())
        if x < 0:
            break
        lista.append(x)
    return lista


def filtrarPares(lista):
    pares = []
    for elem in lista:
        if elem % 2 == 0:
            pares.append(elem)
    return pares


listaFragmentos = poblar()

print(sum(filtrarPares(listaFragmentos)))
