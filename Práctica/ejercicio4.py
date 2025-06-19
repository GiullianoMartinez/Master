"""
 EJERCICIO: RUNAS INESTABLES
Un mago tiene una lista de runas antiguas, cada una con una cantidad de energía (entero positivo o negativo). Las runas inestables son aquellas que:

Tienen energía negativa (corruptas).

Tienen energía impar (inestables).

Las únicas runas que pueden usarse son las que tienen energía positiva y par.

El programa debe:

Leer una lista de enteros.

Filtrar y conservar solo las runas positivas y pares.

Mostrar cuántas runas útiles hay.

Calcular la energía máxima y la mínima de las runas útiles.

Mostrar estos valores.

Si no hay ninguna runa útil, mostrar: "No hay runas estables."

🎯 Requisitos y restricciones (igual que antes):
Los números se ingresan uno por uno.

El ingreso termina cuando el usuario escribe exactamente "fin" (en minúsculas).

No uses try/except, .lower(), .isdigit(), .lstrip().

Solo se aceptan números enteros (positivos, negativos o cero).
"""

def poblar():
    lista = []
    while True:
        x = input()
        if x == "fin":
            break
        numero = int(x)
        lista.append(numero)
    return lista


def filtrarPositivos(lista):
    listaFiltrada = []
    for num in lista:
        if num > 0 and num % 2 == 0:
            listaFiltrada.append(num)
    return listaFiltrada

lista = poblar()
listaParPositiva = filtrarPositivos(lista)

if len(listaParPositiva) == 0:
    print("No hay runas estables.")
else:
    print(f"Cantidad de runas estables: {len(listaParPositiva)}")
    print(f"Energía máxima: {max(listaParPositiva)}")
    print(f"Energía mínima: {min(listaParPositiva)}")

