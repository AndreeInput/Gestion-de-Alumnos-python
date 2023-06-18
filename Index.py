import tkinter as tk
from tkinter import font
import AgregarEstudiante
import ConsultarEstudiante
from styles import *

def abrir_ventana_agregar_estudiante():
    AgregarEstudiante.crear_ventana_agregar_estudiante()
def abrir_ventana_Consultar_estudiante():
    ConsultarEstudiante.Consultar_estudiante()

# Funciones para los botones
def iniciar_aplicacion():
    ventana_bienvenida.destroy()
    # Aquí puedes colocar el código para abrir la ventana principal de tu aplicación
def abrir_ayuda():
    # Aquí puedes colocar el código para abrir una ventana de ayuda o mostrar información adicional
    pass
def salir_aplicacion():
    ventana_bienvenida.destroy()

# Crear la ventana de bienvenida
ventana_bienvenida = tk.Tk()
ventana_bienvenida.title("Sistema de Gestión de Estudiantes - Bienvenida")
ventana_bienvenida.geometry(pantalla)
ventana_bienvenida.resizable(False, False)

# Configurar la fuente del título
titulo_font = font.Font(family=FontFamily, size=FontSizeTitles, weight=FontBold)

# Crear el título
titulo_label = tk.Label(ventana_bienvenida, text="Bienvenido al Sistema",font= titulo_font)
titulo_label.pack(pady=50)

# Crear un marco para contener los botones
marco = tk.Frame(ventana_bienvenida)
marco.pack()

# Configurar la fuente y el tamaño de los botones
boton_font = font.Font(family=FontSizeTitles, size=FontSizeBtn, weight=FontBold)


# Crear los botones con diseño personalizado
boton_iniciar = tk.Button(marco, text="Agregar Estudiante", font=boton_font, bg=colorBtns, fg=colorFont, width=17, height=2,command=abrir_ventana_agregar_estudiante)
boton_iniciar.pack(side=tk.LEFT, padx=10, pady=10)

boton_ayuda = tk.Button(marco, text="Ver Estudiantes", font=boton_font, bg= colorBtns, fg=colorFont, width=17, height=2, command=abrir_ventana_Consultar_estudiante)
boton_ayuda.pack(side=tk.LEFT, padx=10, pady=10)


# Centrar verticalmente el marco
ventana_bienvenida.update()
marco.place(relx=0.5, rely=0.5, anchor="center")

ventana_bienvenida.mainloop()
