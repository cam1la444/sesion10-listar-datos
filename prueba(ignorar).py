import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

ventana_principal = tk.Tk()
ventana_principal.title("prueba")
ventana_principal.geometry("400x400")
ventana_principal.resizable(0, 0)
ventana_principal.config(bg="gray")

ventana_principal.grid_columnconfigure(0, weight=1)
ventana_principal.grid_columnconfigure(1, weight=1)
ventana_principal.grid_columnconfigure(2, weight=1)

marco = tk.LabelFrame(
    ventana_principal,
    text = "Formulario de registro",
    bg = "gray",
    fg = "white",
    font = ("Arial", 12)
)
marco.pack(
    padx = 10,
    pady = 10,
    fill = "both",
    expand = True
)

nombre = tk.Label(
    marco,
    text="prueba",
    bg="gray",
    fg="white",
    font=("Arial", 12)
)
nombre.grid(row=0, column=0, padx=5, pady=(10), sticky="w")

boton = tk.Button(
    marco,
    text = "presioname",
    bg="gray",
    fg="white",
    font=("Arial", 12),
    command=lambda: messagebox.showinfo("Mensaje", "Hola mundo")
)
boton.grid(row=0, column=1, padx=5, pady=(10), sticky="n")

apellido = tk.Label(
    marco,
    text="Apellido",
    bg="gray",
    fg="white",
    font=("Arial", 12)
)
apellido.grid(row=0, column=2, padx=5, pady=(10), sticky="e")

email = tk.Label(
    marco,
    text="Email",
    bg="gray",
    fg="white",
    font=("Arial", 12)
)
email.grid(row=1, column=2, padx=5, pady=(10), sticky="e")

dirreccion = tk.Label(
    marco,
    text = "Direccion",
    bg = "gray",
    fg = "white",
    font = ("Arial", 12)
)
dirreccion.grid(row=1, column=0, padx=5, pady=(10), sticky="w")

ventana_principal.mainloop()

