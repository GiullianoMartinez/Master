def sumatoriaCuadrados(n):
    suma = 0
    for k in range(1, n + 1):
        suma += k ** 2
    return suma

def productoriaPares(n):
    producto = 1
    for k in range(1, n + 1):
        producto *= k * 2
    return producto

def sucesionRecursiva(n):
    a = 1
    for i in range(2, n + 1):
        a = 2 * a + 1
    return a

def serieDeTaylor(x,n):
    suma = 0
    for k in range(n + 1):
        signo = (- 1) ** k
        numerador = x ** (2 * k + 1)
        denominador = factorial(2 * k + 1)
        suma += signo * numerador / denominador
    return suma

def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def cosenoTaylor(x,n):
    suma = 0
    for k in range(n + 1):
        signo =  (-1) ** k
        numerador = x ** (2 * k)
        denominador = factorial( 2 * k)
        suma += signo * numerador / denominador
    return suma


def serieDeTaylor2(x,n):
    suma = 0
    for k in range(n + 1):
        numerador = x ** k
        denominador = factorial(k)
        suma += numerador / denominador
    return suma




