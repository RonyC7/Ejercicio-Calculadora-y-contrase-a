from tkinter import messagebox
from tkinter import *

def verificar_contrasena():
    contrasena = entry_contrasena.get()

    if len(contrasena) < 8:
        messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres.")
        return

    if not any(c.isupper() for c in contrasena) or not any(c.islower() for c in contrasena):
        messagebox.showerror("Error", "La contraseña debe contener al menos 1 letra mayúscula y 1 letra minúscula.")
        return

    if not any(c.isdigit() for c in contrasena) or contrasena[0].isdigit() or contrasena[-1].isdigit():
        messagebox.showerror("Error", "La contraseña debe contener al menos un número, pero no puede ir al principio ni al final.")
        return

    caracteres_especiales = ['!', '@', '#', '$']
    if not any(c in caracteres_especiales for c in contrasena) or contrasena[0] in caracteres_especiales or contrasena[-1] in caracteres_especiales:
        messagebox.showerror("Error", "La contraseña debe contener al menos un carácter especial (!, @, #, $), pero no puede ir al principio ni al final.")
        return

    messagebox.showinfo("Éxito", "La contraseña es válida.")

ventana = Tk()
ventana.title("Verificar Contraseña")
ventana.geometry("300x200")

color_fondo = "#BB8763"
color_botones = "#C39D7A"
color_label = "#BB8763"

ventana.configure(bg=color_fondo)


frame_superior = Frame(ventana, bg=color_fondo, height=50)
frame_superior.pack()

label_contrasena = Label(ventana, text="Contraseña:", bg=color_label)
label_contrasena.pack(pady=10)

entry_contrasena = Entry(ventana, show="*")
entry_contrasena.pack()

boton_verificar = Button(ventana, text="Verificar", command=verificar_contrasena, bg=color_botones)
boton_verificar.pack(pady=10)

ventana.mainloop()
