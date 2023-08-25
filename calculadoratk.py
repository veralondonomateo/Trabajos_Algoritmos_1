from tkinter import*
import math

app = Tk()
app.geometry('1000x1000')
app.config(background='White')

def suma():
    number1 = float(entrada1.get() )
    number2 = float(entrada2.get())
    result = number1 + number2
    resultado.insert(0,result)
def resta():
    number1 = float(entrada1.get() )
    number2 = float(entrada2.get())
    result = number1 - number2
    resultado.insert(0,result)
def multi():
    number1 = float(entrada1.get() )
    number2 = float(entrada2.get())
    result = number1  * number2
    resultado.insert(0,result)

def division():
    number1 = float(entrada1.get() )
    number2 = float(entrada2.get())
    try:
        result = number1  / number2
        resultado.insert(0,result)
    except ZeroDivisionError as error:
        result = f'{error} No es posible dividir entre 0'
        resultado.insert(0,result)

def enterdivision():
    number1 = float(entrada1.get() )
    number2 = float(entrada2.get())
    try:
        result = number1  % number2
        resultado.insert(0,result)
    except ZeroDivisionError as error:
        result = f'{error} No es posible dividir entre 0'
        resultado.insert(0,result)


def sen():
    number1 = int(entrada1.get())
    result = math.sin(math.radians(number1))
    resultado.insert(0,result)

def cos():
    number1 = int(entrada1.get())
    result = math.cos(math.radians(number1))
    resultado.insert(0,result)

def tan():
    number1 = int(entrada1.get())
    result = math.tan(math.radians(number1))
    resultado.insert(0,result)

def delete():
    resultado.delete(0,END)

label1 = Label(app,background='black',text='Ingresa el primer número',fg='white',font=('Times New Roman',30))
entrada1 = Entry(app,background='#943',fg='white',font=('Times New Roman',25),justify=CENTER)
label2 = Label(app,background='black',text='Ingresa el segundo número',fg='white',font=('Times New Roman',30))
entrada2 = Entry(app,background='#943',fg='white',font=('Times New Roman',25),justify=CENTER)
boton1 = Button(app,text='Suma',background='white',fg='black',command= lambda : suma())
boton2 = Button(app,text='Resta',background='white',fg='black',command= lambda: resta())
boton3 = Button(app,text='Multiplicación',background='white',fg='black',command= lambda: multi())
boton4 = Button(app,text='División',background='white',fg='black', bg='gray',command= lambda: division())
boton5 = Button(app,text='División entera',background='white',fg='black',command=lambda: enterdivision())
boton6 = Button(app,text='Seno',background='white',fg='black',command=lambda:sen())
boton7 = Button(app,text='Coseno',background='white',fg='black',command=lambda:cos())
boton8 = Button(app,text='Tangente',bg='white',fg='black',command=lambda:tan())
label3 = Label(app,background='black',text='Resultado',fg='white',font=('Times New Roman',30))
resultado =Entry(app,background='#943',fg='white',font=('Times New Roman',25),justify=CENTER)
botoneliminar = Button(app,text='Borrar',justify='center',font=('Times New Roman',25),command=lambda : delete())


label1.pack(fill=BOTH,expand=True)
entrada1.pack(fill=BOTH,expand=True)
label2.pack(fill=BOTH,expand=True)
entrada2.pack(fill=BOTH,expand=True)
boton1.pack(fill=BOTH,expand=True)
boton2.pack(fill=BOTH,expand=True)
boton3.pack(fill=BOTH,expand=True)
boton4.pack(fill=BOTH,expand=True)
boton5.pack(fill=BOTH,expand=True)
boton6.pack(fill=BOTH,expand=True)
boton7.pack(fill=BOTH,expand=True)
boton8.pack(fill=BOTH,expand=True)
label3.pack(fill=BOTH,expand=True)
resultado.pack(fill=BOTH,expand=True)
botoneliminar.pack(fill=BOTH,expand=True)


app.mainloop()