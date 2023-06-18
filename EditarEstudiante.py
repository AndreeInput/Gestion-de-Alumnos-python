import tkinter as tk
from tkinter import font
import mysql.connector
from styles import *

# Función para obtener los datos del estudiante seleccionado y abrir la ventana de edición
def editar_estudiante(estudiante):
    ventana_edicion = tk.Toplevel()
    ventana_edicion.geometry(pantalla)  
    ventana_edicion.resizable(False, False)
    ventana_edicion.title("Gestión de Usuarios")

    titulo_font = font.Font(family=FontFamily, size=FontSizeTitles, weight=FontBold)
    Campos = font.Font(family=FontFamily, size=FontInput)
    Spaces = font.Font(size=FontSpaces)
    boton_font = font.Font(family=FontSizeTitles, size=FontSizeBtn, weight=FontBold)
    # Crear el título
    titulo_label = tk.Label(ventana_edicion, text="Editar Alumno", font=titulo_font)
    titulo_label.pack(pady=50)
      # Crear los campos de texto y etiquetas para la ventana de edición
    label_nombre = tk.Label(ventana_edicion, text="Nombre:", font=Campos)
    label_nombre.pack()
    entry_nombre = tk.Entry(ventana_edicion, width=30,font=Campos)
    entry_nombre.pack()

    label_edad = tk.Label(ventana_edicion, text="Edad:", font=Campos)
    label_edad.pack()
    entry_edad = tk.Entry(ventana_edicion, width=30,font=Campos)
    entry_edad.pack()

    label_carrera = tk.Label(ventana_edicion, text="Carrera:", font=Campos)
    label_carrera.pack()
    entry_carrera = tk.Entry(ventana_edicion, width=30,font=Campos)
    entry_carrera.pack()

    # Obtener los datos del estudiante seleccionado
    id_estudiante = estudiante[0]
    nombre = estudiante[1]
    edad = estudiante[2]
    carrera = estudiante[3]

    # Preencher los campos de entrada con la información actual del estudiante
    entry_nombre.insert(0, nombre)
    entry_edad.insert(0, edad)
    entry_carrera.insert(0, carrera)

    # Función para guardar los cambios realizados en la edición del estudiante
    def guardar_cambios():
        # Obtener los nuevos valores ingresados en los campos de texto
        nuevo_nombre = entry_nombre.get()
        nueva_edad = entry_edad.get()
        nueva_carrera = entry_carrera.get()

        # Realizar la conexión a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="estudiantespy"
        )

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Ejecutar la consulta para actualizar la información del estudiante
        consulta = "UPDATE estudiantes SET nombre=%s, edad=%s, carrera=%s WHERE id=%s"
        valores = (nuevo_nombre, nueva_edad, nueva_carrera, id_estudiante)
        cursor.execute(consulta, valores)

        # Confirmar los cambios en la base de datos
        connection.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        # Cerrar la ventana de edición
        ventana_edicion.destroy()

    # Crear el botón de guardar cambios
    Spacio = tk.Label(ventana_edicion, text=" ", font=Spaces)
    Spacio.pack()
    boton_guardar = tk.Button(ventana_edicion, text="Guardar Cambios", command=guardar_cambios, font=boton_font,bg=colorBtns, fg=colorFont)
    boton_guardar.pack(side=tk.TOP, padx=10, pady=10)
 
