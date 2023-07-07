from tkinter import *

def calcular_operacion():
    numero1 = float(entry_numero1.get())
    numero2 = float(entry_numero2.get())
    operacion = operacion_var.get()

    if operacion == "suma":
        resultado = numero1 + numero2
    elif operacion == "resta":
        resultado = numero1 - numero2
    elif operacion == "multiplicacion":
        resultado = numero1 * numero2
    elif operacion == "division":
        resultado = numero1 / numero2

    label_resultado.config(text="Resultado: " + str(resultado))


ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("300x200")  

color_fondo = "#FCE4CA"  
color_botones = "#C3A492"  

ventana.configure(bg=color_fondo)

label_numero1 = Label(ventana, text="Número 1:", bg=color_fondo)
label_numero1.pack()

entry_numero1 = Entry(ventana)
entry_numero1.pack()

label_numero2 = Label(ventana, text="Número 2:", bg=color_fondo)
label_numero2.pack()

entry_numero2 = Entry(ventana)
entry_numero2.pack()

operaciones = ["suma", "resta", "multiplicacion", "division"]
operacion_var = StringVar()
operacion_var.set(operaciones[0])

dropdown_operacion = OptionMenu(ventana, operacion_var, *operaciones)
dropdown_operacion.config(bg=color_botones)
dropdown_operacion.pack()

boton_calcular = Button(ventana, text="Calcular", command=calcular_operacion, bg=color_botones)
boton_calcular.pack()

label_resultado = Label(ventana, text="Resultado:", bg=color_fondo)
label_resultado.pack()


ventana.mainloop()
