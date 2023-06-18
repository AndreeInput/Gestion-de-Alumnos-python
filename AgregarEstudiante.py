import tkinter as tk
from tkinter import font
import mysql.connector
from styles import *

def crear_ventana_agregar_estudiante():
    # Función para agregar un nuevo estudiante a la base de datos
    def agregar_estudiante():
        # Obtener los valores ingresados en los campos de texto
        nombre = entry_nombre.get()
        edad = entry_edad.get()
        carrera = entry_carrera.get()

        # Verificar que los campos no estén vacíos
        if nombre.strip() == "":
            mensaje_label.configure(text="El campo Nombre no puede estar vacío", fg="red")
            return
        if edad.strip() == "":
            mensaje_label.configure(text="El campo Edad no puede estar vacío", fg="red")
            return
        if carrera.strip() == "":
            mensaje_label.configure(text="El campo Carrera no puede estar vacío", fg="red")
            return

        # Realizar la conexión a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="estudiantespy"
        )

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Ejecutar la consulta para agregar el nuevo estudiante
        consulta = "INSERT INTO estudiantes (nombre, edad, carrera) VALUES (%s, %s, %s)"
        valores = (nombre, edad, carrera)
        cursor.execute(consulta, valores)

        # Confirmar los cambios en la base de datos
        connection.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        # Limpiar los campos de texto
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_carrera.delete(0, tk.END)

        # Mostrar un mensaje de éxito
        mensaje_label.configure(text="Nuevo estudiante agregado correctamente", fg="green")

     
    ventana_agregar_estudiante = tk.Toplevel()
    ventana_agregar_estudiante.title("Agregar Estudiante")
    ventana_agregar_estudiante.geometry(pantalla)  
    ventana_agregar_estudiante.resizable(False, False)
    
    # Configurar la fuente del título
    titulo_font = font.Font(family=FontFamily, size=FontSizeTitles, weight=FontBold)
    titles_campos= font.Font(family=FontFamily, size=FontInput)
    boton_font = font.Font(family=FontSizeBtn, size=FontSizeBtn, weight=FontBold)
    Spaces = font.Font(size=FontSpaces)
    # Crear el título
    titulo_label = tk.Label(ventana_agregar_estudiante, text="Nuevo Estudiante", font=titulo_font)
    titulo_label.pack(pady=50)
    
    marco = tk.Frame(ventana_agregar_estudiante)
    marco.pack()

    # Crear los campos de texto y etiquetas
    label_nombre = tk.Label(ventana_agregar_estudiante, text="Nombre:", font=titles_campos)
    label_nombre.pack()
    entry_nombre = tk.Entry(ventana_agregar_estudiante, width=30, font=titles_campos)  
    entry_nombre.pack()

    label_edad = tk.Label(ventana_agregar_estudiante, text="Edad:",font=titles_campos)
    label_edad.pack()
    entry_edad = tk.Entry(ventana_agregar_estudiante, width=30,font=titles_campos)  # Cambiar el ancho del campo de texto
    entry_edad.pack()

    label_carrera = tk.Label(ventana_agregar_estudiante, text="Carrera:",font=titles_campos)
    label_carrera.pack()
    entry_carrera = tk.Entry(ventana_agregar_estudiante, width=30,font=titles_campos)  # Cambiar el ancho del campo de texto
    entry_carrera.pack()

    # Crear el botón de agregar estudiante
    Spacio = tk.Label(ventana_agregar_estudiante, text=" ", font=Spaces)
    Spacio.pack()
    boton_agregar = tk.Button(ventana_agregar_estudiante, text="Agregar Estudiante", command=agregar_estudiante,font=boton_font,bg=colorBtns, fg=colorFont, relief="raised")  # Cambiar el tamaño de la fuente y el estilo del botón
    boton_agregar.pack(pady=10)  # Agregar un espacio entre el botón y los campos de texto

    # Etiqueta para mostrar mensajes
    mensaje_label = tk.Label(ventana_agregar_estudiante, fg="green")
    mensaje_label.pack()


    ventana_agregar_estudiante.update()
    marco.place(relx=0.5, rely=0.5, anchor="center")










