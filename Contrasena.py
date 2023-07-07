from tkinter import messagebox
from tkinter import *

def verificar_contrasena():
    contrasena = entry_contrasena.get()

    # Verificar la longitud de la contraseña
    if len(contrasena) < 8:
        messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres.")
        return

    # Verificar si hay al menos 1 letra mayúscula y 1 letra minúscula
    if not any(c.isupper() for c in contrasena) or not any(c.islower() for c in contrasena):
        messagebox.showerror("Error", "La contraseña debe contener al menos 1 letra mayúscula y 1 letra minúscula.")
        return

    # Verificar si hay al menos un número, pero no al principio ni al final
    if not any(c.isdigit() for c in contrasena) or contrasena[0].isdigit() or contrasena[-1].isdigit():
        messagebox.showerror("Error", "La contraseña debe contener al menos un número, pero no puede ir al principio ni al final.")
        return

    # Verificar si hay al menos un carácter especial, pero no al principio ni al final
    caracteres_especiales = ['!', '@', '#', '$']
    if not any(c in caracteres_especiales for c in contrasena) or contrasena[0] in caracteres_especiales or contrasena[-1] in caracteres_especiales:
        messagebox.showerror("Error", "La contraseña debe contener al menos un carácter especial (!, @, #, $), pero no puede ir al principio ni al final.")
        return

    # Contraseña válida
    messagebox.showinfo("Éxito", "La contraseña es válida.")

# Crear la ventana
ventana = Tk()
ventana.title("Verificar Contraseña")
ventana.geometry("300x200")  

color_fondo = "#FCE4CA"  
color_botones = "#C3A492"  

ventana.configure(bg=color_fondo)

# Crear los widgets
label_contrasena = Label(ventana, text="Contraseña:")
label_contrasena.pack()

entry_contrasena = Entry(ventana, show="*")
entry_contrasena.pack()

boton_verificar = Button(ventana, text="Verificar", command=verificar_contrasena)
boton_verificar.pack()

# Iniciar la ventana principal
ventana.mainloop()
