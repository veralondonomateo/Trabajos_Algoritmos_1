import functools
import promedio 
print('*'*50)
print('BIENVENIDO A SUPERMERCADO SAULITO')
print('*'*50)

productos = {
    "Leche":1000,

    "Pan":800,
    
    "Huevos":1200,
    
    "Arroz":4500,
    
    "Pasta":2500,
    
    "Aceite de oliva":4200,
    
    "Pollo":9500,
    
    "Carne molida":3000,
    
    "Pescado":7000,
    
    "Manzanas":3000,
    
    "Plátanos":2500,
    
    "Naranjas":1000,
    
    "Zanahorias":800,
    
    "Brócoli":300,
    
    "Espinacas":400,
    
    "Queso":9000,
    
    "Yogur":5000,
    
    "Cereal":3000,
    
    "Galletas":4000,
    
    "Papas":150,
    
    "Salsa de tomate":3200,
    
    "Sopa enlatada":2300,
    
    "Detergente para ropa":3500,
    
    "Jabón de baño":6000
}
print(productos)

elecciones = []
new_var = []
def productos1():
    eleccion = input('Que producto deseas elegir => ').title()
    new_var.append(eleccion)
    if eleccion in productos.keys():
        eleccion_v1 = productos[eleccion]
        return elecciones.append(eleccion_v1)
    else:
        print('Elige un producto valido')
        productos1()
    
productos1()


while True:
    eleccion_final = input('¿Deseas otro producto? ').lower()
    if eleccion_final == 'si':
        productos1()
    else:
        break

total_final = functools.reduce(lambda x,y : x+y, elecciones)
print(f'Total de la factura {total_final}')
promedio = total_final / len(elecciones)
print(f'Su promedio de compra {promedio}')