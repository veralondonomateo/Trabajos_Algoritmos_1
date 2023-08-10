print('CONOCE LOS FACTORES PRIMOS DE UN NÚMERO')

def factor_primo():
    factores = []
    var_1 = 0
    var_2 = 0
    election = int(input('ingresa el numero a evaluar => '))
    while election > var_1:
        var_1 += 1
        if election % var_1 == 0:
            x = 0
            y = 0
            while var_1 > x:
                x += 1
                if var_1 % x == 0:
                    y += 1
                else: 
                    pass
            if y > 2:
                pass
            else:
                factores.append(var_1)  
                    
            var_2 += 1
        else:
            pass
    print('Sus factores primos son',factores)

factor_primo()

while True:
    election = input('¿Deseas probar con tro numero? ').lower()
    if election == 'si':
        factor_primo()
    else:
        break