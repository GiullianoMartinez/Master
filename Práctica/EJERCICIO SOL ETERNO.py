def esPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def esImpar(n):
    return n % 2 == 1


def esPerfecto(n):
    sumaDivisores = 0
    for i in range(1, n):
        if n % i == 0:
            sumaDivisores += i
    return n == sumaDivisores


def contieneDigito7(n):
    while n > 0:
        ultDigito = n % 10
        if ultDigito == 7:
            return True
        n //= 10
    return False


def puedeEstabilizarSol(nucleosRecolectados,sumaNucleos,mayorNucleo):
    return esPrimo(nucleosRecolectados) and esImpar(sumaNucleos) and esPerfecto(mayorNucleo) and contieneDigito7(sumaNucleos)


def calcularPorcentaje(parcial,total):
    if total == 0:
        return 0.0
    return (parcial/total) * 100


def main():
    numeroAprendiz = 1
    totalAprendiz = 0
    estabilizaron = 0
    noEstabilizaron = 0

    while True:
        nombre = input()
        if nombre == "X":
            break

        nucleosRecolectados = int(input())

        i = 0
        sumaNucleos = 0
        mayorNucleo = -1
        while i < nucleosRecolectados:
            nucleo = int(input())
            sumaNucleos += nucleo
            
            if nucleo > mayorNucleo:
                mayorNucleo = nucleo
            i += 1
        
        print(f"""APRENDIZ #{numeroAprendiz} --> {nombre}
TOTAL NÚCLEOS = {nucleosRecolectados}
SUMA TOTAL DE ENERGÍA = {sumaNucleos}
MAYOR VALOR DE NÚCLEO = {mayorNucleo}""")
        
        if puedeEstabilizarSol(nucleosRecolectados,sumaNucleos,mayorNucleo):
            print("SI PUEDE ESTABILIZAR EL SOL ETERNO")
            estabilizaron += 1
        else:
            print("NO PUEDE ESTABILIZAR EL SOL ETERNO")
            noEstabilizaron += 1
        print("-----------------------------------------------")

        numeroAprendiz += 1
        totalAprendiz += 1

    print(f"""REPORTE FINAL
=============
TOTAL DE APRENDICES PROCESADOS: {totalAprendiz}  
% QUE ESTABILIZARON EL SOL ETERNO = {round(calcularPorcentaje(estabilizaron,totalAprendiz), 2)}  
% QUE NO LO ESTABILIZARON = {calcularPorcentaje(noEstabilizaron,totalAprendiz)}  """)
        
