"""
EJERCICIO: CRISTALES CORRUPTOS
Un alquimista analiza una lista de cristales mágicos. Cada cristal tiene una energía representada por un 
un número entero. Los cristales negativos están corruptos y deben ser descartados. Además, 
los cristales con energía cero no sirven para nada y también deben eliminarse.

El programa debe:

Leer una lista de números enteros.

Eliminar los valores negativos y los ceros.

Contar cuántos cristales válidos quedan.

Calcular el promedio de sus energías.

Mostrar ambos resultados.

Requisitos y restricciones:
Los números se ingresan uno por uno.

El ingreso termina cuando el usuario escribe exactamente "fin" (en minúsculas).

No uses try/except, ni .lower(), ni .isdigit(), ni .lstrip().

Solo se aceptan números enteros (positivo, negativo o cero).

Si no hay cristales válidos (todos son cero o negativos), mostrar un mensaje especial: "No hay cristales útiles."

"""
def poblar():
    lista = []
    while True:
        ingreso = input()
        if ingreso == "fin":
            break
        numero = int(ingreso)
        lista.append(numero)
    return lista


def listaPositiva(lista):
    listaNueva = []
    for num in lista:
        if num > 0:
            listaNueva.append(num)
    return listaNueva
    

listaCristales = poblar()
nuevaLista = listaPositiva(listaCristales)

if len(nuevaLista) == 0:
    print("No hay cristales útiles.")

else:
    print(f"La nueva lista es {nuevaLista}")
    print(f"Quedan {len(nuevaLista)} cristales válidos")

    print(f"El promedio de sus energías es {round(sum(nuevaLista) / len(nuevaLista), 2)}")




