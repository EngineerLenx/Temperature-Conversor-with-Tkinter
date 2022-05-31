from tkinter import *
from tkinter import ttk
#Ventana
root = Tk()
root.title("Conversor de temperatura")
root.geometry("400x100")
root.config(bg = "dark gray")
root.resizable(0, 0)
root.iconphoto(False, PhotoImage(file='C:/Users/luern/Downloads/images.png'))

#Entrada de datos (grados)
TempE = ttk.Entry(root, width= 10)
TempE.place(x = 80, y = 60)

#Funcion de conversión
def Conversion():
    #Un try-except pa evitar que el usuario ingrese un dato tipo string
    try:
        TempEntrada = TempIn.get()
        TempSalida = TempOut.get()
        grades = float(TempE.get())
        if TempEntrada == TempSalida:
            resultado = grades
        elif TempEntrada == "Fahrenheit" and TempSalida == "Celsius":
            resultado = (grades -32) * 5.0/9.0
        elif TempEntrada == "Celsius" and TempSalida == "Fahrenheit":
            resultado = (9.0/5.0 * grades +32)
        elif TempEntrada == "Celsius" and TempSalida == "Kelvin":
            resultado = (grades + 273.15)
        elif TempEntrada == "Kelvin" and TempSalida == "Celsius":
            resultado = (grades - 273.15)
        elif TempEntrada == "Fahrenheit" and TempSalida == "Kelvin":
            resultado = (grades-32)*5/9+273.15
        elif TempEntrada == "Kelvin" and TempSalida == "Fahrenheit":
            resultado = (grades-273.15)*9/5+32

        #Formato para que muestre puntos decimales limitadamente
        salida_result.config(text = '{:.5}'.format(resultado))
    except ValueError:
        pass

#Funcion para eliminar datos
def clean_all():
    TempE.delete(0, END)
    TempE.insert(0, " ")
    salida_result.config(text = "")

#Petición
Peticion = Label(root, text = "Elige la escala de temperatura e ingresa los datos necesarios:")
Peticion.config(bg = "dark gray")
Peticion.place(x = 40, y = 0)

#Combobox de entrada de la conversión
TempIn = StringVar()
ComboIn = ttk.Combobox(root, width= 10, state = "readonly", textvariable= TempIn)
ComboIn.place(x = 71 , y = 30)
ComboIn["values"] = ("Fahrenheit", "Celsius", "Kelvin")
ComboIn.current(0)

#Combobox de salida de la conversión
TempOut = StringVar()
ComboOut = ttk.Combobox(root, width= 10, state = "readonly", textvariable = TempOut)
ComboOut.place(x = 250, y = 30)
ComboOut["values"] = ("Celsius", "Fahrenheit", "Kelvin")
ComboOut.current(0)

#Botón de conversión
button = ttk.Button(root, text = "Convertir \n      ➜", command = Conversion, width=10)
button.place(x = 167, y = 40)

#Label de Salida (muestra el resultado)
salida_result = ttk.Label(root, text = "", width = 5)
salida_result.place(x = 270, y = 60)

#Botón de borrado
clean = ttk.Button(root, text="Borrar", command = clean_all, width = 7)
clean.place(x = 340, y = 70)

#Ejecución de la ventana, siempre al final del código.
root.mainloop()