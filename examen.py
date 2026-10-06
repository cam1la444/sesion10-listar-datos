import tkinter as tk
from tkinter import messagebox, ttk

# =========================================================================
# 1. ESTRUCTURAS DE DATOS BÁSICAS DE PYTHON (LISTAS, DICCIONARIOS, TUPLAS)
# =========================================================================

# --- LISTA SIMPLE (Indexada por posición) ---
lista_paises = ["El Salvador", "México", "España", "Colombia", "Argentina"]

# --- DICCIONARIO (Clave: Valor) ---
# Se utiliza para consultar roles y los permisos asociados
diccionario_roles = {
    "Administrador": "Acceso Total",
    "Usuario": "Acceso Limitado",
    "Invitado": "Solo Lectura"
}

# --- LISTA DE DICCIONARIOS (Estructura de datos principal / BD temporal) ---
# Cada elemento es un registro representado por un diccionario
base_datos_usuarios = [
    {"id": 1, "nombre": "Ana Gómez", "edad": 22, "pais": "El Salvador", "genero": "Femenino", "rol": "Administrador"},
    {"id": 2, "nombre": "Carlos Ruiz", "edad": 30, "pais": "México", "genero": "Masculino", "rol": "Usuario"}
]


# =========================================================================
# 2. CONFIGURACIÓN DE LA VENTANA PRINCIPAL DE TKINTER
# =========================================================================
ventana = tk.Tk()
ventana.title("Guía Completa Tkinter + Fundamentos de Python")
ventana.geometry("620x860")
ventana.resizable(0, 0)
ventana.config(bg="#1e1e2e")

# MARCO PRINCIPAL (LabelFrame - Mega Marco Decorativo)
marco_principal = tk.LabelFrame(
    ventana,
    text=" SISTEMA INTEGRADO (TKINTER + ESTRUCTURAS DE DATOS) ",
    font=("Arial", 11, "bold"),
    bg="#2a2a3c",
    fg="#89b4fa",
    bd=2,
    relief="groove"
)
marco_principal.pack(padx=15, pady=15, fill="both", expand=True)

# Configuración de 3 columnas dentro del marco para distribuir espacio con .grid()
marco_principal.grid_columnconfigure(0, weight=1)
marco_principal.grid_columnconfigure(1, weight=1)
marco_principal.grid_columnconfigure(2, weight=1)


# =========================================================================
# 3. VARIABLES DINÁMICAS DE TKINTER
# =========================================================================
var_genero = tk.StringVar(value="Masculino")
var_acepta = tk.BooleanVar(value=False)
var_edad = tk.IntVar(value=18)
var_pais = tk.StringVar(value=lista_paises[0])  # Uso del primer elemento de la lista
var_rol = tk.StringVar(value=list(diccionario_roles.keys())[0])  # Obtener primera clave del diccionario


# =========================================================================
# 4. ENCABEZADO Y ALINEACIÓN EN GRID (sticky: nw, n, ne)
# =========================================================================
tk.Label(marco_principal, text="Guía v3.0", bg="#2a2a3c", fg="#a6e3a1", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nw")
tk.Label(marco_principal, text="Formulario + Python", bg="#2a2a3c", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=(10, 5), sticky="n")
tk.Label(marco_principal, text="Estado: Online", bg="#2a2a3c", fg="#f9e2af", font=("Arial", 10, "italic")).grid(row=0, column=2, padx=10, pady=(10, 5), sticky="ne")


# =========================================================================
# 5. FORMULARIO (ENTRY, SPINBOX, OPTIONMENU, CHECKBUTTON, RADIOBUTTON)
# =========================================================================
# --- Entry (Campo de texto de 1 línea) ---
tk.Label(marco_principal, text="Nombre:", bg="#2a2a3c", fg="white", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_nombre = tk.Entry(marco_principal, bg="#1e1e2e", fg="white", insertbackground="white")
entry_nombre.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

# --- Spinbox (Selector numérico con límites) ---
tk.Label(marco_principal, text="Edad:", bg="#2a2a3c", fg="white", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
spin_edad = tk.Spinbox(marco_principal, from_=1, to=100, textvariable=var_edad, width=5, bg="#1e1e2e", fg="white")
spin_edad.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# --- OptionMenu leyendo datos desde la LISTA 'lista_paises' ---
tk.Label(marco_principal, text="País (desde Lista):", bg="#2a2a3c", fg="white", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
dropdown_pais = tk.OptionMenu(marco_principal, var_pais, *lista_paises)
dropdown_pais.config(bg="#1e1e2e", fg="white", highlightthickness=0)
dropdown_pais.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="w")

# --- OptionMenu leyendo datos desde las claves del DICCIONARIO 'diccionario_roles' ---
tk.Label(marco_principal, text="Rol (desde Diccionario):", bg="#2a2a3c", fg="white", font=("Arial", 10)).grid(row=4, column=0, padx=10, pady=5, sticky="w")
dropdown_rol = tk.OptionMenu(marco_principal, var_rol, *list(diccionario_roles.keys()))
dropdown_rol.config(bg="#1e1e2e", fg="white", highlightthickness=0)
dropdown_rol.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky="w")

# --- Radiobuttons (Selección Única) ---
frame_radio = tk.Frame(marco_principal, bg="#2a2a3c")
frame_radio.grid(row=5, column=0, columnspan=3, pady=5)
tk.Label(frame_radio, text="Género:", bg="#2a2a3c", fg="white").pack(side="left", padx=5)
tk.Radiobutton(frame_radio, text="M", variable=var_genero, value="Masculino", bg="#2a2a3c", fg="white", selectcolor="#1e1e2e").pack(side="left")
tk.Radiobutton(frame_radio, text="F", variable=var_genero, value="Femenino", bg="#2a2a3c", fg="white", selectcolor="#1e1e2e").pack(side="left")

# --- Checkbutton (Casilla Booleana) ---
check_terminos = tk.Checkbutton(marco_principal, text="Acepto los términos y condiciones", variable=var_acepta, bg="#2a2a3c", fg="white", selectcolor="#1e1e2e")
check_terminos.grid(row=6, column=0, columnspan=3, pady=5)

# --- Text Widget (Campo Multilínea) ---
tk.Label(marco_principal, text="Observaciones (Text):", bg="#2a2a3c", fg="white", font=("Arial", 9)).grid(row=7, column=0, columnspan=3, sticky="w", padx=10)
campo_texto_largo = tk.Text(marco_principal, height=3, width=40, bg="#1e1e2e", fg="white", insertbackground="white")
campo_texto_largo.grid(row=8, column=0, columnspan=3, padx=10, pady=5, sticky="ew")


# =========================================================================
# 6. LÓGICA DE PYTHON (FUNCIONES, CONDICIONALES Y MANIPULACIÓN DE DICCIONARIOS)
# =========================================================================
def guardar_registro():
    # Métodos de cadena en Python: .strip() quita espacios, .title() convierte a mayúscula inicial
    nombre_ingresado = entry_nombre.get().strip().title()
    edad_ingresada = var_edad.get()
    pais_ingresado = var_pais.get()
    genero_ingresado = var_genero.get()
    rol_ingresado = var_rol.get()
    acepta_terminos = var_acepta.get()

    # --- ESTRUCTURA CONDICIONAL DE VALIDACIÓN (IF / ELIF / ELSE) ---
    if not nombre_ingresado:
        messagebox.showwarning("Atención", "El nombre no puede estar vacío.")
    elif len(nombre_ingresado) < 3:
        messagebox.showwarning("Atención", "El nombre debe tener al menos 3 caracteres.")
    elif not acepta_terminos:
        messagebox.showerror("Error", "Debes aceptar los términos para continuar.")
    else:
        # BÚSQUEDA EN DICCIONARIO: Obtener valor por su clave (.get)
        permisos = diccionario_roles.get(rol_ingresado, "Sin Permisos")

        # CREACIÓN DE UN NUEVO DICCIONARIO CON LOS DATOS DE ENTRADA
        nuevo_usuario = {
            "id": len(base_datos_usuarios) + 1,
            "nombre": nombre_ingresado,
            "edad": edad_ingresada,
            "pais": pais_ingresado,
            "genero": genero_ingresado,
            "rol": rol_ingresado
        }

        # AGREGAR EL DICCIONARIO A LA LISTA
        base_datos_usuarios.append(nuevo_usuario)

        # INSERTAR LOS DATOS DENTRO DE LA TABLA (TREEVIEW)
        tabla.insert("", tk.END, values=(
            nuevo_usuario["id"],
            nuevo_usuario["nombre"],
            nuevo_usuario["edad"],
            nuevo_usuario["pais"],
            nuevo_usuario["genero"],
            nuevo_usuario["rol"]
        ))

        # LIMPIEZA DE CAMPOS DE FORMULARIO
        entry_nombre.delete(0, tk.END)
        campo_texto_largo.delete("1.0", tk.END)
        
        # MENSAJE INFORMATIVO DE CONFIRMACIÓN
        messagebox.showinfo("Éxito", f"Usuario '{nombre_ingresado}' guardado.\nPermisos asignados: {permisos}")


# Botón Guardar Registro
btn_guardar = tk.Button(
    marco_principal, text=" Guardar Registro ", bg="#89b4fa", fg="#11111b",
    font=("Arial", 10, "bold"), cursor="hand2", command=guardar_registro
)
btn_guardar.grid(row=9, column=0, columnspan=3, pady=10)


# =========================================================================
# 7. TABLA DE DATOS (TTK.TREEVIEW) Y RECORRIDO DE LISTA DE DICCIONARIOS
# =========================================================================
# TUPLA con los nombres de las columnas de la tabla (Inmutable)
columnas = ("id", "nombre", "edad", "pais", "genero", "rol")

tabla = ttk.Treeview(marco_principal, columns=columnas, show="headings", height=4)

# Configuración de encabezados con un BUCLE FOR recorriendo la TUPLA 'columnas'
for col in columnas:
    tabla.heading(col, text=col.capitalize())

tabla.column("id", width=30, anchor="center")
tabla.column("nombre", width=100)
tabla.column("edad", width=40, anchor="center")
tabla.column("pais", width=80)
tabla.column("genero", width=70, anchor="center")
tabla.column("rol", width=90, anchor="center")

tabla.grid(row=10, column=0, columnspan=3, padx=10, pady=5, sticky="ew")


# --- BUCLE FOR 1: Cargar la LISTA DE DICCIONARIOS inicial dentro de la tabla ---
for usuario in base_datos_usuarios:
    # Construcción de una TUPLA de valores para insertar en la tabla
    valores = (usuario["id"], usuario["nombre"], usuario["edad"], usuario["pais"], usuario["genero"], usuario["rol"])
    tabla.insert("", tk.END, values=valores)


# --- BUCLE FOR 2: Vaciar el widget Treeview y limpiar la lista ---
def vaciar_todo():
    # Recorrer todos los IDs de la tabla de Tkinter para borrarlos
    for item in tabla.get_children():
        tabla.delete(item)
    
    # Vaciar la lista de Python usando el método .clear()
    base_datos_usuarios.clear()
    
    messagebox.showinfo("Tabla Limpia", "Se han borrado todos los registros de la tabla y de la lista.")

btn_limpiar = tk.Button(marco_principal, text="Vaciar Tabla y Lista", bg="#f38ba8", fg="#11111b", font=("Arial", 9, "bold"), command=vaciar_todo)
btn_limpiar.grid(row=11, column=0, columnspan=3, pady=(0, 10))


# =========================================================================
# 8. CANVAS (ÁREA PARA DIBUJAR FIGURAS GEOMÉTRICAS Y TEXTO)
# =========================================================================
tk.Label(marco_principal, text="Área de Dibujo (Canvas):", bg="#2a2a3c", fg="white", font=("Arial", 9)).grid(row=12, column=0, columnspan=3, sticky="w", padx=10)

lienzo = tk.Canvas(marco_principal, width=350, height=40, bg="#1e1e2e", highlightthickness=1, highlightbackground="#89b4fa")
lienzo.grid(row=13, column=0, columnspan=3, pady=5)

# Dibujo por coordenadas (x1, y1, x2, y2)
lienzo.create_rectangle(10, 10, 80, 30, fill="#a6e3a1", outline="")
lienzo.create_oval(100, 10, 130, 30, fill="#f9e2af", outline="")
lienzo.create_line(150, 20, 220, 20, fill="#f38ba8", width=2)
lienzo.create_text(270, 20, text="Tkinter + Python", fill="white", font=("Arial", 9, "bold"))


# Iniciar el bucle principal de ejecución de la interfaz gráfica
ventana.mainloop()