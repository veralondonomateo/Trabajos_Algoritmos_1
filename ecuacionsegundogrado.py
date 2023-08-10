"""import math

a = 2.0
b = -7.0
c = 3.0
raiz = ((b**2)-((4*a)*c))** 0.5
determinante = ((b**2)-((4*a)*c))
if determinante < 0:
    print('Los dijitos hacen que el determinante sea negativo')
else:
    x1 = (-1 * b + ((b**2)-4*(a)*c) ** 0.5) / (2 * a)
    x2 =( -1 * b - ((b**2)-4*(a)*c) ** 0.5) / (2 * a)
    print(f'los resultados son {x1} y {x2}')"""

# Control of errors

import math 
def secondgrade():
    a = float(input('Chooise a one number => '))
    b = float(input('Chooise a one number => '))
    c = float(input('Chooise a one number => '))
    

    try: 
        determinante = math.sqrt((b**2) - (4*a*c)) 
        x1 = -1*b + determinante / (2*a)
        x2 = -1*b - determinante / (2*a)
        print(f'Result are {x1} and {x2}')
    except ValueError as error:
        print(error)
        print('The determinate is negative that´s why reason the sqrt lose')
        election = input('You want make with other numbers? ').lower()
        if election == 'si' or election == 'yes':
            secondgrade()
        elif election == 'no' or election == 'don´t':
            exit
        
secondgrade()