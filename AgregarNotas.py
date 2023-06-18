import tkinter as tk
import mysql.connector
from tkinter import font
from styles import *

# Función para agregar una nota al estudiante
def agregar_nota(estudiante):
    # Obtén el ID del estudiante
    id_estudiante = estudiante[0]

    # Ventana emergente para ingresar la nota
    ventana_nota = tk.Toplevel()
    ventana_nota.title("Agregar Nota")
    ventana_nota.geometry(pantalla)  
    ventana_nota.resizable(False, False)

    # Etiqueta y campo de entrada para la nota

    titulo_font = font.Font(family=FontFamily, size=FontSizeTitles, weight=FontBold)
    Campos = font.Font(family=FontFamily, size=FontInput)
    Spaces = font.Font(size=FontSpaces)
    boton_font = font.Font(family=FontSizeTitles, size=FontSizeBtn, weight=FontBold)
    # Crear el título
    titulo_label = tk.Label(ventana_nota, text="Nueva Calificacion:",font= titulo_font)
    titulo_label.pack(pady=50)

    label_materia = tk.Label(ventana_nota, text="Materia:" ,font= Campos)
    label_materia.pack()
    entrada_materia = tk.Entry(ventana_nota,font= Campos)
    entrada_materia.pack()

    label_nota = tk.Label(ventana_nota, text="Nota:" ,font= Campos)
    label_nota.pack()
    entrada_nota = tk.Entry(ventana_nota,font= Campos)
    entrada_nota.pack()

    # Función para guardar la nota en la base de datos
    def guardar_nota():
        # Obtén el valor de la nota ingresada
        nota = entrada_nota.get()
        Materia = entrada_materia.get()

        # Realiza la conexión a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="estudiantespy"
        )

        # Crea un cursor para ejecutar consultas
        cursor = connection.cursor()
        # Ejecuta la consulta para agregar la nota del estudiante
        consulta = "INSERT INTO notas (id_estudiante, materia, nota) VALUES (%s, %s, %s)"
        valores = (id_estudiante,Materia,nota)
        cursor.execute(consulta,valores)

        # Confirma los cambios en la base de datos
        connection.commit()
        # Cierra el cursor y la conexión
        cursor.close()
        connection.close()

        # Cierra la ventana emergente
        ventana_nota.destroy()

    # Botón para guardar la nota
    Spacio = tk.Label(ventana_nota, text=" ", font=Spaces)
    Spacio.pack()
    boton_guardar = tk.Button(ventana_nota, text="Guardar", command=guardar_nota, font=boton_font,bg=colorBtns, fg=colorFont)
    boton_guardar.pack()


