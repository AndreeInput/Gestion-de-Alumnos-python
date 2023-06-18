import tkinter as tk
from tkinter import font
import mysql.connector
from styles import *

# Función para mostrar las notas del estudiante seleccionado
def mostrar_notas(estudiante):
    # Obtén el ID del estudiante
    id_estudiante = estudiante[0]

    # Realiza la conexión a la base de datos
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="estudiantespy"
    )

    # Crea un cursor para ejecutar consultas
    cursor = connection.cursor()

    # Ejecuta la consulta para obtener las notas del estudiante
    consulta = "SELECT materia, nota FROM notas WHERE id_estudiante = %s"
    valores = (id_estudiante,)
    cursor.execute(consulta, valores)

    # Obtiene todas las notas del estudiante
    notas = cursor.fetchall()

    # Crea una ventana emergente para mostrar las notas
    ventana_notas = tk.Toplevel()
    ventana_notas.title("Notas del Estudiante")
    ventana_notas.geometry(pantalla)
    ventana_notas.resizable(False, False)

    # Etiqueta para mostrar las notas
    titulo_font = font.Font(family=FontFamily, size=FontSizeTitles, weight=FontBold)
    Campos = font.Font(family=FontFamily, size=FontInput)

    etiqueta_notas = tk.Label(ventana_notas, text="Notas del Estudiante:", font=titulo_font)
    etiqueta_notas.pack()

    # Texto enriquecido para mostrar las notas
    texto_notas = tk.Text(ventana_notas, height=10, width=30 , font=Campos)
    texto_notas.pack()

    # Inserta las notas en el texto enriquecido
    for nota in notas:
        texto_notas.insert(tk.END, str(nota[0]) +" :"+" "+ str(nota[1]) + "\n")

    # Deshabilita la edición del texto enriquecido
    texto_notas.configure(state="disabled")

    # Cierra el cursor y la conexión
    cursor.close()
    connection.close()


