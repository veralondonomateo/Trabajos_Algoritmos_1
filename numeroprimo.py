print('CALCULADORA NÚMEROS PRIMOS')
print('Podras saber si el número que ingreses es primo o compuesto\n')

def primos():
    num_election = int(input('Ingresa el número a evaluar => '))

    var_x = 0
    var_y = 0

    while num_election > var_x:
        var_x += 1
        if num_election % var_x == 0:
            var_y += 1
        else:
            pass
    
    if var_y > 2:
            print(f'el {num_election} es compuesto')
    else:
            print(f'el {num_election} es primo')

primos()

while True:
    election_continous = input('¿Deseas continuar? ')
    election_continous = election_continous.lower()
    if election_continous == 'si':
        primos()
    else:
        break

