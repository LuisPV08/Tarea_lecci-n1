import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Diccionario para almacenar los alumnos
alumnos = {}

# Función para calcular la calificación según la nota
def calcular_calificacion(nota):
    if nota < 5:
        return "SS"
    elif 5 <= nota < 7:
        return "AP"
    elif 7 <= nota < 9:
        return "NT"
    elif nota >= 9:
        return "SB"

# Función para mostrar todos los alumnos
def mostrar_alumnos():
    # Limpiar la tabla antes de mostrar nuevos datos
    for row in treeview.get_children():
        treeview.delete(row)
    
    for dni, info in alumnos.items():
        treeview.insert("", "end", values=(dni, info["apellidos"], info["nombre"], info["nota"], info["calificacion"]))

# Función para introducir un nuevo alumno
def introducir_alumno():
    dni = entry_dni.get()
    if dni in alumnos:
        messagebox.showerror("Error", "Ya existe un alumno con ese DNI.")
        return
    apellidos = entry_apellidos.get()
    nombre = entry_nombre.get()
    try:
        nota = float(entry_nota.get())
    except ValueError:
        messagebox.showerror("Error", "La nota debe ser un número.")
        return
    calificacion = calcular_calificacion(nota)
    alumnos[dni] = {"apellidos": apellidos, "nombre": nombre, "nota": nota, "calificacion": calificacion}
    messagebox.showinfo("Éxito", "Alumno agregado correctamente.")
    mostrar_alumnos()

# Función para eliminar un alumno por su DNI
def eliminar_alumno():
    dni = entry_dni.get()
    if dni in alumnos:
        del alumnos[dni]
        messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
    else:
        messagebox.showerror("Error", "Alumno no encontrado.")
    mostrar_alumnos()

# Función para consultar la nota y la calificación de un alumno
def consultar_alumno():
    dni = entry_dni.get()
    if dni in alumnos:
        alumno = alumnos[dni]
        label_resultado.config(text=f"Nota: {alumno['nota']} Calificación: {alumno['calificacion']}")
    else:
        messagebox.showerror("Error", "Alumno no encontrado.")

# Función para modificar la nota de un alumno
def modificar_nota():
    dni = entry_dni.get()
    if dni in alumnos:
        try:
            nueva_nota = float(entry_nota.get())
        except ValueError:
            messagebox.showerror("Error", "La nota debe ser un número.")
            return
        alumnos[dni]["nota"] = nueva_nota
        alumnos[dni]["calificacion"] = calcular_calificacion(nueva_nota)
        messagebox.showinfo("Éxito", "Nota modificada correctamente.")
    else:
        messagebox.showerror("Error", "Alumno no encontrado.")
    mostrar_alumnos()

# Función para mostrar los alumnos suspensos
def mostrar_suspensos():
    # Limpiar la tabla antes de mostrar los suspensos
    for row in treeview.get_children():
        treeview.delete(row)

    for dni, info in alumnos.items():
        if info["calificacion"] == "SS":
            treeview.insert("", "end", values=(dni, info["apellidos"], info["nombre"], info["nota"], info["calificacion"]))

# Función para mostrar los alumnos aprobados
def mostrar_aprobados():
    # Limpiar la tabla antes de mostrar los aprobados
    for row in treeview.get_children():
        treeview.delete(row)

    for dni, info in alumnos.items():
        if info["calificacion"] != "SS":
            treeview.insert("", "end", values=(dni, info["apellidos"], info["nombre"], info["nota"], info["calificacion"]))

# Función para mostrar los candidatos a matrícula de honor (nota 10)
def mostrar_candidatos_mh():
    # Limpiar la tabla antes de mostrar los candidatos a matrícula de honor
    for row in treeview.get_children():
        treeview.delete(row)

    for dni, info in alumnos.items():
        if info["nota"] == 10:
            treeview.insert("", "end", values=(dni, info["apellidos"], info["nombre"], info["nota"], info["calificacion"]))

# Función para modificar la calificación de un alumno
def modificar_calificacion():
    dni = entry_dni.get()
    if dni in alumnos:
        # Calculamos la calificación basada en la nota actual
        alumnos[dni]["calificacion"] = calcular_calificacion(alumnos[dni]["nota"])
        messagebox.showinfo("Éxito", "Calificación modificada correctamente.")
    else:
        messagebox.showerror("Error", "Alumno no encontrado.")
    mostrar_alumnos()

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Calificaciones de Alumnos")
ventana.geometry("800x600")

# Configuración del frame principal para organización
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=20)

# Etiquetas y campos de entrada
label_dni = tk.Label(frame_entrada, text="DNI:")
label_dni.grid(row=0, column=0, padx=10, pady=5)
entry_dni = tk.Entry(frame_entrada)
entry_dni.grid(row=0, column=1, padx=10, pady=5)

label_apellidos = tk.Label(frame_entrada, text="Apellidos:")
label_apellidos.grid(row=1, column=0, padx=10, pady=5)
entry_apellidos = tk.Entry(frame_entrada)
entry_apellidos.grid(row=1, column=1, padx=10, pady=5)

label_nombre = tk.Label(frame_entrada, text="Nombre:")
label_nombre.grid(row=2, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(frame_entrada)
entry_nombre.grid(row=2, column=1, padx=10, pady=5)

label_nota = tk.Label(frame_entrada, text="Nota:")
label_nota.grid(row=3, column=0, padx=10, pady=5)
entry_nota = tk.Entry(frame_entrada)
entry_nota.grid(row=3, column=1, padx=10, pady=5)

# Botones de las funciones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

btn_introducir = tk.Button(frame_botones, text="Introducir Alumno", width=20, command=introducir_alumno)
btn_introducir.grid(row=0, column=0, padx=10, pady=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Alumno", width=20, command=eliminar_alumno)
btn_eliminar.grid(row=0, column=1, padx=10, pady=5)

btn_consultar = tk.Button(frame_botones, text="Consultar Alumno", width=20, command=consultar_alumno)
btn_consultar.grid(row=1, column=0, padx=10, pady=5)

btn_modificar_nota = tk.Button(frame_botones, text="Modificar Nota", width=20, command=modificar_nota)
btn_modificar_nota.grid(row=1, column=1, padx=10, pady=5)

# Botones para mostrar resultados
frame_resultados = tk.Frame(ventana)
frame_resultados.pack(pady=20)

btn_suspensos = tk.Button(frame_resultados, text="Mostrar Suspensos", width=20, command=mostrar_suspensos)
btn_suspensos.grid(row=0, column=0, padx=10, pady=5)

btn_aprobados = tk.Button(frame_resultados, text="Mostrar Aprobados", width=20, command=mostrar_aprobados)
btn_aprobados.grid(row=0, column=1, padx=10, pady=5)

btn_candidatos_mh = tk.Button(frame_resultados, text="Mostrar Candidatos a MH", width=20, command=mostrar_candidatos_mh)
btn_candidatos_mh.grid(row=1, column=0, padx=10, pady=5)

btn_modificar_calificacion = tk.Button(frame_resultados, text="Modificar Calificación", width=20, command=modificar_calificacion)
btn_modificar_calificacion.grid(row=1, column=1, padx=10, pady=5)

# Treeview para mostrar los resultados
frame_treeview = tk.Frame(ventana)
frame_treeview.pack(pady=20)

# Crear el Treeview para mostrar los alumnos
treeview = ttk.Treeview(frame_treeview, columns=("DNI", "Apellidos", "Nombre", "Nota", "Calificación"), show="headings")
treeview.heading("DNI", text="DNI")
treeview.heading("Apellidos", text="Apellidos")
treeview.heading("Nombre", text="Nombre")
treeview.heading("Nota", text="Nota")
treeview.heading("Calificación", text="Calificación")

treeview.column("DNI", width=100)
treeview.column("Apellidos", width=150)
treeview.column("Nombre", width=150)
treeview.column("Nota", width=100)
treeview.column("Calificación", width=100)

treeview.pack()

# Ejecutar la aplicación
ventana.mainloop()
