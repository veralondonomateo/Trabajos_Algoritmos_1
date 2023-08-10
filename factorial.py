print('CALCULA DE FORMA FACTORIAL UN NUMERO')

#Función para calcular el factorial con un parametro n
def factorial(n):
    if n == 1:
        resultado = 1
    elif n == 0:
        resultado = 0

    if n > 1:
        #Resolviendo el factorial con el sistema 4! = 4*3*2*1
        resultado = n * factorial(n - 1)

    #Retorno  ala función factorial con su parametro n
    return resultado

election = int(input('Ingresa el número a evaluar'))
result = factorial(election)
print(f'El factorial de {election} es {result}')