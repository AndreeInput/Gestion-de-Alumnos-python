import tkinter as tk
from tkinter import font
import mysql.connector
import EditarEstudiante
import ElimarEstudiante
import AgregarNotas
import MostrarNotas
import Informes
from styles import *

def Consultar_estudiante():
    ventana_Consulta = tk.Toplevel()
    # Crear la ventana principal
    ventana_Consulta.geometry(pantalla)  
    ventana_Consulta.resizable(False, False)
    ventana_Consulta.title("Gestión de Usuarios")
    # Crear el título
    titulo_fontone = font.Font(family=FontFamily, size=FontSizeTitles, weight=FontBold)
    titulo_font = font.Font(family=FontFamily, size=FontInput)

    titulo_label = tk.Label(ventana_Consulta, text="Informacion de Alumnos", font=titulo_fontone)
    titulo_label.pack(pady=50)

    # Crear la lista de usuarios
    lista_usuarios = tk.Listbox(ventana_Consulta)
    lista_usuarios.pack()

    # Función para obtener la información del usuario seleccionado
    def obtener_informacion_usuario(usuario):
        # Aquí puedes realizar la acción que desees al obtener la información del usuario seleccionado
        print("Información del usuario:", usuario)
        EditarEstudiante.editar_estudiante(usuario)
        ventana_Consulta.destroy()

    # Función para eliminar un usuario
    def eliminar_usuario(usuario):
        # Aquí puedes realizar la acción que desees al eliminar el usuario
        print("Eliminar usuario:", usuario)
        ElimarEstudiante.eliminar_estudiante(usuario)
        ventana_Consulta.destroy()

    # Función para agregar calificaciones a un usuario
    def agregar_calificaciones(usuario):
        # Aquí puedes realizar la acción que desees al agregar calificaciones al usuario
        print("Agregar calificaciones a usuario:", usuario)
        AgregarNotas.agregar_nota(usuario)

    def Mostrar_NotasALumno(usuario):
        # Aquí puedes realizar la acción que desees al agregar calificaciones al usuario
        print("Agregar calificaciones a usuario:", usuario)
        MostrarNotas.mostrar_notas(usuario)

    def Generar_Informe(usuario):
        # Aquí puedes realizar la acción que desees al agregar calificaciones al usuario
        print("Agregar calificaciones a usuario:", usuario)
        Informes.generar_reporte(usuario)


    # Función para actualizar la lista de usuarios
    def actualizar_lista_usuarios():
        # Borrar los elementos actuales de la lista
        lista_usuarios.delete(0, tk.END)

        # Realizar la conexión a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="estudiantespy"
        )

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Ejecutar la consulta para obtener los usuarios
        consulta = "SELECT * FROM estudiantes"
        cursor.execute(consulta)

        # Obtener los resultados de la consulta
        usuarios = cursor.fetchall()
        boton_font = font.Font(family=FontSizeTitles, size=FontSizeBtn2, weight=FontBold)

        # Iterar sobre los usuarios y agregarlos a la lista
        for usuario in usuarios:
            # Crear un Frame para agrupar la información del usuario y los botones
            frame_usuario = tk.Frame(lista_usuarios)
            frame_usuario.pack(fill="x")

            # Mostrar la información del usuario
            label_usuario = tk.Label(frame_usuario, text=usuario[1], font=titulo_font)
            label_usuario.pack(side="left", padx=10)

            # Botón para editar la información del usuario
            boton_editar = tk.Button(frame_usuario, text="Editar",font=boton_font, bg= colorBtns, fg=colorFont, command=lambda u=usuario: obtener_informacion_usuario(u))
            boton_editar.pack(side="left", padx=5)

            # Botón para eliminar al usuario
            boton_eliminar = tk.Button(frame_usuario, text="Eliminar",font=boton_font, bg= colorBtns, fg=colorFont, command=lambda u=usuario: eliminar_usuario(u))
            boton_eliminar.pack(side="left", padx=5)

            # Botón para agregar calificaciones al usuario
            boton_calificaciones = tk.Button(frame_usuario, text="Agregar Calificaciones",font=boton_font, bg= colorBtns, fg=colorFont, command=lambda u=usuario: agregar_calificaciones(u))
            boton_calificaciones.pack(side="left", padx=5)

            # Botón para mostrar las calificaciones
            MostrarCali = tk.Button(frame_usuario, text="Ver Calificaciones",font=boton_font, bg= colorBtns, fg=colorFont, command=lambda u=usuario: Mostrar_NotasALumno(u))
            MostrarCali.pack(side="left", padx=5)

            # Botón para Generar Informe
            InformeBtn = tk.Button(frame_usuario, text="Generar Informe",font=boton_font, bg= colorBtns, fg=colorFont, command=lambda u=usuario: Generar_Informe(u))
            InformeBtn.pack(side="left", padx=5)

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

   # Actualizar la lista de usuarios al iniciar la aplicación
    actualizar_lista_usuarios()
