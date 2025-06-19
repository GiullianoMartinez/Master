def esParMayorA4(n):
    if n < 5:
        return False
    return n % 2 == 0


def esMultiploDe3(n):
    return n % 3 == 0


def esPalindromo(n):
    original = n
    reverso = 0
    while n > 0:
        ultDigito = n % 10
        reverso = reverso * 10 + ultDigito
        n //= 10
    return reverso == original


def contieneDigito4(n):
    while n > 0:
        ultDigito = n % 10
        if ultDigito == 4:
            return True
        n //= 10
    return False


def calcularPorcentaje(parcial,total):
    if total == 0:
        return 0.0
    return (parcial/total) * 100


def puedeActivarLote(uno,dos,tres,cuatro):
    return esParMayorA4(uno) and esMultiploDe3(dos) and esPalindromo(tres) and contieneDigito4(cuatro)



def main():
    numeroTecnico = 1
    totalTecnico = 0
    puedeActivar = 0
    noPuedeActivar = 0
    while True:
        nombre = input()
        if nombre == "CIERRE":
            break

        cantidadFragmentos = int(input())

        i = 0
        menorFragmento = 999
        sumaFragmentos = 0
        while i < cantidadFragmentos:
            fragmento = int(input())
            sumaFragmentos += fragmento
            if fragmento < menorFragmento:
                menorFragmento = fragmento
            i += 1
        
        promedio = sumaFragmentos // cantidadFragmentos

        print(f"""TÉCNICO #{numeroTecnico} --> {nombre}
TOTAL FRAGMENTOS = {cantidadFragmentos}
SUMA ENERGÉTICA = {sumaFragmentos}
MENOR FRAGMENTO = {menorFragmento}
PROMEDIO TRUNCADO = {promedio}""")
        
        if puedeActivarLote(cantidadFragmentos,sumaFragmentos,menorFragmento,promedio):
            print("SI PUEDE CERTIFICAR EL LOTE ENERGÉTICO")
            puedeActivar += 1
        else:
            print("NO PUEDE CERTIFICAR EL LOTE ENERGÉTICO")
            noPuedeActivar += 1

        print("----------------------------------------------")

        numeroTecnico += 1
        totalTecnico += 1
    
    print(f"""REPORTE FINAL
=============
TOTAL DE TÉCNICOS PROCESADOS: {totalTecnico}
% QUE CERTIFICARON LOTE = {round(calcularPorcentaje(puedeActivar,totalTecnico), 2)}
% QUE NO CERTIFICARON LOTE = {round(calcularPorcentaje(noPuedeActivar,totalTecnico), 2)}""")

main()