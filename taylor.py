import math

def funcion_original(x):
    # Define la función original que quieres aproximar mediante la serie de Taylor
    # Por ejemplo, vamos a utilizar la función seno (puedes cambiarla por la que necesites)
    return math.sin(x)

def derivada_n(funcion, a, n):
    # Calcula la n-ésima derivada de la función en el punto "a"
    h = 1e-5
    return (funcion(a + h*n) - funcion(a)) / (h**n)

def serie_de_taylor(funcion, a, num_terminos):
    # Calcula la aproximación de la función mediante la serie de Taylor alrededor del punto "a"
    aproximacion = 0
    for n in range(num_terminos):
        aproximacion += derivada_n(funcion, a, n) * (x - a)**n / math.factorial(n)
    return aproximacion

# Punto donde queremos aproximar la función
a = 0

# Número de términos en la serie de Taylor (cuantos más términos, mayor precisión)
num_terminos = 5

# Valor de "x" para calcular la aproximación
x = 2

# Aproximación de la función mediante la serie de Taylor
aproximacion = serie_de_taylor(funcion_original, a, num_terminos)

# Resultado
print(f"Aproximación de la función en x={x}: {aproximacion}")
print(f"Valor real de la función en x={x}: {funcion_original(x)}")