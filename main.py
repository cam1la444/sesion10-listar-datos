import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#lista de estudiantes
"""
Esta lista almacenara todos los estuidantes registrados.
Cada vez que se registre un estudiante, se creara un diccionario con sus datos y 
ese diccionario se agregara a esta lista mediante append()
"""

estudiantes = []

#funcion para centrar una ventana
def centrar_ventana(ventana, ancho, altura):
    ventana.update_idletask() #se actualiza la ventana para que tkinter conozca correctamente las dimensiones y posicion.

    #obtener la posicion de la ventana principal
    posicion_x = ventana_principal.winfo_x() #winfoxx obtiene la posicion horizontal de la ventana principal en la pantalla
    posicion_y = ventana_principal.winfo_y() #winfo y obtiene la posicion vertical

    #obtener tamaño de la ventana principal
    ancho_principal = ventana_principal.winfo_width() #obtiene el ancho actual de la ventana principal
    alto_principal = ventana_principal.winfo_height() #obtiene el alto actual de la ventana principal

    #calcular la posicion del formulario
    x = posicion_x+ (ancho_principal - ancho) //2
    y = posicion_y + (alto_principal - altura) //2

    #restablecer tamaño y posicion
    ventana.geometry( #geometry permite indicar el ancho x alto + posicion x + posicion y
        f"{ancho}x{altura}+{x}+{y}"
        )

#FUNCION PARA MOSTRAR ESTUDIANTES
def mostrar_estudiantes():
    #limpiar ventana
    #treeview mantiene sus registros visualmente. antes de volver a mostrar la info eliminamos todos los registros existentes de la tabla
    for registro in tabla.get_childer():
        tabla.delete(registro)

    #recorrer la lista de estudiantes
    #cada elemento de la lista es un diccionario que contiene la info de un estudiante
    for estudiante in estudiantes:
        #obtener datos del diccionario
        #para obtener un dato utilizamos su CLAVE, y la clave funciona como el nombre del dato.
        tabla.insert(
            "",
            tk.END, #o 0 para indicar que los registros aparezcan al inicio, asi como esta lo agrega al final
            values=(
                estudiante["nombre"],
                estudiante["apellido"],
                estudiante["dui"],
                estudiante["telefono"],
                estudiante["correo"],
                estudiante["edad"],
                estudiante["genero"],
                estudiante["carrera"]
                )
            )

#FUNCION PARA AGREGAR ESTUDIANTE
def agregar_estudiante():
    #para crear ventana secundaria
    ventana = tk.Toplevel( #topleve permite crear una segunda ventana relacionada con la ventana principal
        ventana_principal
    )
    ventana.title(
        "Agregar estudiante"
    )

    #tamaño de la ventana
    ancho = 750
    altura= 700

    #CENTRAR ventana. llamamos a la funcion para colocar el formulario en el centro de la ventana principal
    centrar_ventana(
        ventana,
        ancho,
        altura
        )

    ventana.resizable( #configuracion de la ventana
        False,
        False
        )

#MANTENER EL FORMULARIO SOBRE LA VENTANA PRINCIPAL
ventana.transient(
    ventana_principal #transient establece una relacion entre las ventana. se indica que ventana pertenece a ventana_principal
)

ventana.grab_set() #grab set hace que el usuario trabaje primero con esta vetana, se conoce como VENTANA MODAL

ventana.focus_force() #coloca el cursis de atencion sobre la vetnana del formulario. de esta forma el a formulario aparece activo

#VARIABLES
nombre = tk.StringVar()
apellido = tk.StringVar()
dui = tk.StringVar()
telefono = tk.StringVar()
correo = tk.StringVar()
genero = tk.StringVar()
carrera = tk.StringVar()
edad = tk.IntVar(value=18)

#TITULO
titulo = tk.Label(
    ventana,
    text="REGISTRO DE ESTUDIANTE",
    font=("Arial", 16, "bold", "underlined")
)
titulo.pack(pady=15)

#FORMULARIO
formulario = tk.Frame(
        ventana
    )

formulario.pack(
        padx=20,
        pady=10
    )

#NOMBRE
tk.Label(
    formulario,
    text="Nombre:"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8,
    sticky="e")
tk.Entry(
    formulario,
    textvariable=nombre,
    width=40
).grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)

#APELLIDO
tk.Label(
    formulario,
    text="Apellido:"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8,
    sticky="e")
tk.Entry(
    formulario,
    textvariable= apellido,
    width=40
).grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)

#DUI
tk.Label(
    formulario,
    text="DUI:",
).grid(
    row=2,
    column=0,
    padx=10,
    pady=8,
    sticky="e"
)
tk.Entry(
    formulario,
    textvariable=dui,
    width=40
).grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)

#TELEFONO
tk.Label(
    formulario,
    text="Telefono:"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=8,
    sticky="e"
)
tk.Entry(
    formulario,
    textvariable=telefono,
    width=40
).grid(
    row=3,
    column=1,
    padx=10,
    pady=8
)

#CORREO
tk.Label(
    formulario,
    text="Correo:"
).grid(
    row=4,
    column=0,
    pady=8,
    padx=10,
    sticky="e"
)
tk.Entry(
    formulario,
    textvariable=correo,
    width=40
).grid(
    row=4,
    column=1,
    padx=10,
    pady=8
)

#EDAD
tk.Label(
    formulario,
    text="Edad:"
).grid(
    row=5,
    column=0,
    pady=8,
    padx=10,
    sticky="e"
)
tk.Spinbox(
    formulario,
    from_=15,
    to=80,
    textvariable=edad,
    width=37
).grid(
    row=5,
    column=1,
    padx=10,
    pady=8
)

#Genero
tk.label(
    formulario,
    text = "Genero:"
).grid(
    row = 6,
    column = 0,
    padx = 10,
    pady = 8,
    sticky = "e"
)
frame_genero = tk.Frame(
    formulario
)
frame_genero.grid(
    row = 6,
    column = 1,
    padx = 10,
    pady = 8,
    sticky = "w"
)
tk.Radiobutton(
    frame_genero,
    text = "Masculino",
    variable = genero,
    value = "Masculino"
).pack(
    side = "left"
)

tk.Radiobutton(
    frame_genero,
    text = "Femenino",
    variable = genero,
    vaalue = "Femenino"
).pack(
    side = "left"
)

#Carrera