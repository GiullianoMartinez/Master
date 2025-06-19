c1 = float(input("Nota certamen 1: "))
guia1 = float(input("Nota guía práctica 1: "))
lab1 = float(input("Nota laboratorio 1: "))
c2 = float(input("Nota certamen 2: "))
guia2 = float(input("Nota guía práctica 2: "))
lab2 = float(input("Nota laboratorio 2: "))
c3 = float(input("Nota certamen 3: "))
guia3 = float(input("Nota guía práctica 3: "))
lab3 = float(input("Nota laboratorio 3: "))
print()

notas = [c1, guia1, lab1, c2, guia2, lab2, c3, guia3, lab3]

modulo1 = c1 * 0.6 + lab1 * 0.3 + guia1 * 0.1
modulo2 = c2 * 0.6 + lab2 * 0.3 + guia2 * 0.1
modulo3 = c3 * 0.6 + lab3 * 0.3 + guia3 * 0.1

np = modulo1 * 0.3 + modulo2 * 0.35 + modulo3 * 0.35
print(f"Tu nota de presentación a examen es: {round(np,2)}")

if all(nota >= 4 for nota in notas) and np >= 5:
    nf = round(np,2)
    print(f"Te has eximido del examen, tu nota final es {nf}")
else:
    print("TIENES QUE DAR EXAMEN")
    print()
    nExamen = float(input("Nota Examen: "))
    nf = round(np * 0.6 + nExamen * 0.4,2)
    print()
    print(f"Tu nota final es {nf}")
    print()
    if nf >= 4:
        print("Aprobaste la asignatura")
        print()
    else:
        print("Reprobaste la asignatura")
        print()

