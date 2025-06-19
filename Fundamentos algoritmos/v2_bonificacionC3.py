categorias = ['LATAM', 'GOLD', 'GOLD PLUS', 'PLATINUM', 'BLACK', 'BLACK SIGNATURE']
multNacional = [3, 4, 5, 7, 8, 9]
multInternacional = [5, 6 , 7, 9, 10, 11]


def procesarSocio(cantSocios):

    DatosSocio = []

    for i in range(cantSocios):
        rut = input()
        categoria = input()

        totalMillas = 0
        totalDolares = 0
        contNacional = contSudamerica = contInternacional = 0

        while True:
            codigoReserva = input()
            if codigoReserva == 'FINISH':
                break

            tipoViaje = int(input())
            montoViaje = int(input())

            totalDolares += montoViaje

            # Determinar multiplicador
            buscarCategoria = categorias.index(categoria)

            if tipoViaje in [1, 2]:
                multiplicador = multNacional[buscarCategoria]
            else:
                multiplicador = multInternacional[buscarCategoria]

            totalMillas += montoViaje * multiplicador

            if tipoViaje == 1:
                contNacional += 1
            elif tipoViaje == 2:
                contSudamerica += 1
            elif tipoViaje == 3:
                contInternacional += 1

        DatosSocio.append((rut, categoria, totalMillas, totalDolares, contNacional, contSudamerica, contInternacional))
    maxMillas = max(DatosSocio, key=lambda x: x[2])[2]
    minMillas = min(DatosSocio, key=lambda x: x[2])[2]

    maxRuts = [s[0] for s in DatosSocio if s[2] == maxMillas]
    minRuts = [s[0] for s in DatosSocio if s[2] == minMillas] 


    return sorted(DatosSocio), maxMillas, minMillas, maxRuts, minRuts





cantSocios = int(input())
listaSocios, maxMillas, minMillas, maxRuts, minRuts = procesarSocio(cantSocios)

print(f'Se procesarán {cantSocios} socios LATAM pass.')
print()
print('==============================================')
print('LISTA DE TUPLAS DATOS SOCIOS ORDENADAS POR RUT')
print('==============================================')
print()
print('RUT - CATEGORIA - TOTAL MILLAS- DOLARES GASTADOS - TOTAL NAC. - TOTAL SUDAM. - TOTAL INTERN.')

for socios in listaSocios:
    print(socios)

print()
print(f'Los siguientes socios acumularon la mayor cantidad de millas = {maxMillas}')
print(f'Lista Rut = {maxRuts}')
print()
print(f'Los siguientes socios acumularon la menor cantidad de millas = {minMillas}')
print(f'Lista Rut = {minRuts}')
print()
print('RESUMEN POR CATEGORÍA')
print('=====================')

for i, categoria in enumerate(categorias):
    sociosCategoria = []
    for socios in listaSocios:
        if socios[1] == categoria:
            sociosCategoria.append(socios)
    
    if sociosCategoria:
        totalMillasCat = sum(socios[2] for socios in sociosCategoria)
        promedio = round(totalMillasCat / len(sociosCategoria))
        print(f'{categoria} - {len(sociosCategoria)} socios - total millas = {totalMillasCat} ==> promedio millas = {promedio}')
    else:
        print(f"{categoria} - NO hay socios en esta categoría")


tiposViaje = [0, 0, 0]

for s in listaSocios:
    tiposViaje[0] += s[4]
    tiposViaje[1] += s[5]
    tiposViaje[2] += s[6]

print()
print('RESUMEN POR TIPO DE VIAJE')
print('=========================')

for i in range(3):
    if tiposViaje[i] > 0:
        print(f'tipo {i + 1} : {tiposViaje[i]} viaje(s)')
    else:
        print(f"tipo {i+1} : NO hay viajes de este tipo")

maxDinero = max(listaSocios, key=lambda x: x[3])[3]
socioMaxDinero = [s[0] for s in listaSocios if s[3] == maxDinero] 

print()
print('MÁXIMO MONTO DÓLARES GASTADO POR SOCIO')
print(f'Máximo monto dólares = US$ {maxDinero}')
print(f'Lista de socios con máximo monto dólares gastado : {socioMaxDinero}')
print()

viajesPorSocio = [(s[0], s[4] + s[5] + s[6]) for s in listaSocios]
maxViajes = max(viajesPorSocio, key=lambda x: x[1])[1]
sociosMaxViajes = [rut for rut, cant in viajesPorSocio if cant == maxViajes]

print('MÁXIMA CANTIDAD DE VIAJES POR SOCIO')
print(f'Máxima cantidad de viajes de socios es: {maxViajes}')
print(f'Lista de socios con máxima cantidad de viajes : {sociosMaxViajes}')






