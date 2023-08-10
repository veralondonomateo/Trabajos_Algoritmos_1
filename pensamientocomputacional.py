#Cambio de todo a minuscula = Entendiendo que todo objeto de string es un funcion ()

"""nombre = input('Ingresa tu nombre =>')
nombre = nombre.lower()
if nombre == 'mateo':
    print('Que bello nombre')
elif nombre == 'carlos':
    print('Que gran historia tiene tu nombre')
 

# Cambio de todo tipo de string a mayuscula entendiendo que upper es una función

variable = input('Ingresa tu nombre: ')"""
 
print('Hello, this is a program for calculate your IMC')

def IBM(peso, altura):
    result = peso / altura ** 2
    return result
peso = float(input('What´s your weigth in kg? '))
print(f'your weigth is {peso}KG')
altura = float(input('What´s your heigth in meters? '))
print(f'your heigth is {altura}M')
print('Your IMB is',IBM(peso,altura))
x = IBM(peso,altura)
if x < 16:
    print('You have severe thinness ')
elif 16.1 < x < 17:
    print('You have moderade thinness')
elif  17.1 < x < 18.5:
    print('You have acceptable thinnes')
elif  18.51 < x < 25:
    print('You have a normal weigth')
elif 25.1 < x < 30:
    print('You have overweigth') 
elif 30.1 < x < 34.99:
    print('You´re obese type one')
elif 35 < x < 40:
    print('You´re obese type two')
else:
    print('Your obese type three')