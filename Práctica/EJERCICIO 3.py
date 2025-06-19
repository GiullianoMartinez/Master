def esPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def esCompuestoImpar(n):
    if n < 3:
        return False

    if esPrimo(n):
        return False
    return n % 2 == 1


def esPerfecto(n):
    sumaDiv = 0
    for i in range(1, n):
        if n % i == 0:
            sumaDiv += i
    return sumaDiv == n


def contieneDigitoPar(n):
    while n > 0:
        ultDigito = n % 10
        if ultDigito % 2 == 0:
            return True
        n //= 10
    return False


def esPalindromo(n):
    original = n
    reverso = 0
    while n > 0:
        ultDigito = n % 10
        reverso = reverso * 10 + ultDigito
        n//= 10
    return reverso == original


def calcularPorcentaje(parcial,total):
    if total == 0:
        return 0.0
    return (parcial/total) * 100


def esNucleoPuro(uno,dos,tres,cuatro):
    return esCompuestoImpar(uno) and esPerfecto(dos) and contieneDigitoPar(tres) and esPalindromo(cuatro)


def main():
    numeroCientifico = 1
    totalCientifico = 0
    puros = 0
    noPuros = 0

    while True:
        nombre = input()
        if nombre == "X":
            break
        totalNucleo = int(input())        
        i = 0
        sumaNucleos = 0
        mayorNucleo = 0

        while i < totalNucleo:
            nucleo = int(input())
            sumaNucleos += nucleo
            if nucleo > mayorNucleo:
                mayorNucleo = nucleo
            i += 1
        promedio = sumaNucleos // totalNucleo

        print(f"""CIENTÍFICO #{numeroCientifico} --> {nombre}
TOTAL NÚCLEOS = {totalNucleo}
SUMA ENERGÍA = {sumaNucleos}
MAYOR NÚCLEO = {mayorNucleo}
PROMEDIO TRUNCADO = {promedio}""")
        
        if esNucleoPuro(totalNucleo,sumaNucleos,mayorNucleo,promedio):
            print("SI ES UN NÚCLEO PURO")
            print("---------------------------------")
            puros += 1

        else:
            print("NO ES UN NÚCLEO PURO")
            print("---------------------------------")
            noPuros += 1
    
        numeroCientifico += 1
        totalCientifico += 1
    
    print(f"""REPORTE FINAL
===================
TOTAL PROCESADOS: {totalCientifico}
% PUROS = {calcularPorcentaje(puros,totalCientifico)}
% NO PUROS = {calcularPorcentaje(noPuros,totalCientifico)}""")

main()

        

    
