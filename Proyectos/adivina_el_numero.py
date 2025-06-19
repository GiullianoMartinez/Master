import random

def seleccionar_nivel():
    while True:
        try:
            nivel = int(input("Elige entre nivel 1, 2 o 3: "))
            if nivel == 1:
                print("Has elegido el nivel fácil: Adivina un número entre [1 y 10]")
                return 1, 10
            elif nivel == 2:
                print("Has elegido el nivel medio: Adivina un número entre [1 y 50]")
                return 1, 50
            elif nivel == 3:
                print("Has elegido el nivel difícil: Adivina un número entre [1 y 100]")
                return 1, 100
            else:
                print("Nivel inválido. Empezarás con el nivel fácil.")
                return 1, 10
        except ValueError:
            print("Por favor ingresa un número válido.")

def jugar():
    while True:
        minimo, maximo = seleccionar_nivel()
        numeroAzar = random.randint(minimo, maximo)
        contIntentos = 0

        while True:
            entrada = input(f'\nAdivina el número entre {minimo} y {maximo} (o escribe "REPETIR" para reiniciar, "SALIR" para terminar): ').strip().upper()
            contIntentos += 1

            if entrada == "REPETIR":
                print("Reiniciando el juego...\n")
                break  # Sale del bucle interno, y vuelve a empezar desde nivel
            elif entrada == "SALIR":
                print("¡Gracias por jugar!")
                return
            else:
                try:
                    intentoUsuario = int(entrada)
                    if intentoUsuario > numeroAzar:
                        print("Te has pasado, el número es menor que", intentoUsuario)
                    elif intentoUsuario < numeroAzar:
                        print("Te has quedado corto, el número es más grande que", intentoUsuario)
                    else:
                        print()
                        print(f"🎉 ¡FELICIDADES! Has acertado en {contIntentos} intentos.\n")
                        break  # Adivinó el número
                except ValueError:
                    print("Entrada no válida. Ingresa un número o una palabra clave ('REPETIR', 'SALIR').")

# Iniciar el juego
jugar()
