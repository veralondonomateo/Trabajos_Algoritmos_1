from tkinter import*
import math

app = Tk()
app.title('Calculadora')
app.config(background='white')

entrada1 = IntVar(app)
entrada2 = IntVar(app)



def suma():
    numero1 = int(entrada1.get())
    numero2 = int(entrada2.get())
    ecuacion = numero1 + numero2
    resultado.insert(0,ecuacion)
    
def resta():
    numero1 = int(entrada1.get())
    numero2 = int(entrada2.get())
    ecuacion = numero1 - numero2
    resultado.insert(0,ecuacion)
def miulti():
    numero1 = int(entrada1.get())
    numero2 = int(entrada2.get())
    ecuacion = numero1 * numero2
    resultado.insert(0,ecuacion)
def division():
    numero1 = int(entrada1.get())
    numero2 = int(entrada2.get())

    try:
        ecuacion = numero1 / numero2
        resultado.insert(0,ecuacion)
        
    except ZeroDivisionError as error:
        x =  f'{error} No se puede dividir por cero'
        resultado.insert(0,x)
        
    

    
def seno():
    numero1 = int(entrada1.get())
    result = math.sin(math.radians(numero1))
    resultado.insert(0,result)

    
def borrar():
    resultado.delete(0,END)

Label(
    
    app,
    text='Escribe el primer número',
    font = ('Times New Roman',59),
    bg='black',
    fg= 'white',

).pack(
    fill=BOTH
)

Entry(
    app,
    font = ('Times New Roman',30),
    justify= 'center',
    bg='gray',
    fg= 'white',  
    textvariable=entrada1
    
).pack(
    fill = BOTH,
)
Label(
    app,
    text='Escribe el segundo número',
    font = ('Times New Roman',59),
    bg='black',
    fg= 'white',

).pack(
    fill = BOTH,
    expand= False)
Entry(
    app,
    font = ('Times New Roman',30),
    justify= 'center',
    bg='gray',
    fg= 'white',  
    textvariable=entrada2
).pack(
    fill = BOTH,
)
Button(
    app,
    text='Suma',
    font=('Times New Roman',30),
    bg='white',
    fg='black',
    command= lambda : suma()
).pack(
    fill = BOTH,)
Button(
    app,
    text='Resta',
    font=('Times New Roman',30),
    bg='white',
    fg='black',
    command= lambda : resta()
    
).pack(
    fill = BOTH,)
Button(
    app,
    text='Multiplicación',
    font=('Times New Roman',30),
    bg='white',
    fg='black',
    command= lambda : miulti()
).pack(
    fill = BOTH,)
boton4 = Button(
    app,
    text='Division',
    font=('Times New Roman',30),
    bg='white',
    fg='black',
    command= lambda:division()
    
   
).pack(
    fill = BOTH,)
boton3 = Button(
    app,
    text='Seno',
    font=('Times New Roman',30),
    bg='white',
    fg='black',
    command= lambda : seno()
).pack(
    fill = BOTH,)

Label(
    
    app,
    text='Respuesta',
    font = ('Times New Roman',59),
    bg='black',
    fg= 'white',

).pack(
    fill = BOTH,
    expand= False)

resultado = Entry(
    app,
    font = ('Times New Roman',30),
    justify= 'center',
    bg='gray',
    fg= 'white', 
        
)
resultado.pack( fill = BOTH, expand= False)


Button(
    app,
    text='Borrar',
    font=('Times New Roman',30),
    bg='white',
    fg='black',
    command= borrar
    
).pack(
    fill = BOTH,)




app.mainloop()
