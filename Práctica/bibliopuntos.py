def poblar():
    categorias = ['ESTUDIANTE', 'ADULTO', 'ADULTO MAYOR']
    tiposLibro = [1, 2, 3]  # (1) Ficción, (2) No ficción, (3) Técnico

    puntajes = [
        [10, 12, 15]  # Estudiante
        [8, 10, 12]   # Adulto
        [6, 8, 10]    # Adulto mayor
    ]


    cantUsuarios = int(input())
    usuarios = []    # Lista de tuplas (rut, categoria)
    tiposPorUsuario = []   # Lista de listas de tipos de libros


    for i in range(cantUsuarios):
        rut = input()
        categoria = input()
        usuarios.append((rut, categoria))
        tipos = []

        while True:
            libro = input()
            if libro == 'FINISH':
                break

            tipo = int(input())
            tipos.append(tipo)

        tiposPorUsuario.append(tipos)

    resumen = []

    for i in range(cantUsuarios):
        rut, categoria = usuarios[i]
        tipos = tiposPorUsuario[i]

        indexCategorias = categorias.index(categoria)

        puntos = 0
        conteo = [0, 0, 0] # [ficcion, no ficcion, tecnico]

        for tipo in tiposLibro:

            indexTipo = tipo - 1  # tipo 1 --> indice 0
            puntos += puntajes[indexCategorias][indexTipo]
            conteo[indexTipo] += 1
        
        totalLibros = sum(conteo)
        resumen.append((rut, puntos, totalLibros, conteo[0], conteo[1], conteo[2]))
    
    resumen.sort()

    print('LISTA ORDENADA POR RUT:')
    print('RUT - PUNTOS - TOTAL LIBROS - FICCION - NO FICCION - TECNICO')

    for dato in resumen:
        print(dato)        


poblar()

