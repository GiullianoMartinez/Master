"""
1. NINJA CHUNNIN

Una academia ninja entrega puntajes a sus estudiantes luego de una misión. Cada estudiante recibe un número entero que representa su desempeño. El programa debe:

Leer una lista de puntajes (enteros).

Eliminar los puntajes duplicados (dejar solo uno de cada uno).

Ordenar la lista de mayor a menor.

Retornar el segundo puntaje más alto.

Ejemplo:

Entrada: [55, 90, 75, 90, 100, 55, 80]
Salida: 90

"""
def eliminarDuplicados(lista):
    sinDuplicados = []
    for elem in lista:
        if elem not in sinDuplicados:
            sinDuplicados.append(elem)
    return sinDuplicados


def segundoMayor(lista):
    listaSinRepetidos = eliminarDuplicados(lista)
    listaSinRepetidos.sort(reverse=True)
    return listaSinRepetidos[1]


listaPuntajes = [55, 90, 75, 90, 100, 55, 80]
print(segundoMayor(listaPuntajes))
