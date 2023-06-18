from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import mysql.connector
from styles import *

# Función para generar el reporte en PDF
def generar_reporte(estudiante):
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
    consulta = "SELECT materia ,nota FROM notas WHERE id_estudiante = %s"
    valores = (id_estudiante,)
    cursor.execute(consulta, valores)

    # Obtiene todas las notas del estudiante
    notas = cursor.fetchall()

    # Genera el nombre del archivo PDF basado en el nombre del estudiante
    nombre_archivo = f"Reporte_{estudiante[1]}_{estudiante[2]}.pdf"

    # Crea el archivo PDF
    c = canvas.Canvas(nombre_archivo, pagesize=letter)

    # Título del reporte
    c.setFont(FontFamily, FontSizeTitles)
    c.drawString(100, 700, "Reporte de Notas")

    # Información del estudiante
    c.setFont(FontFamily, 17)
    c.drawString(100, 650, f"Estudiante:{estudiante[1]}")
    c.drawString(100, 625, f"Carrera:{estudiante[3]}")

    # Notas del estudiante
    c.setFont(FontFamily, FontSizeBtn)
    y = 600
    for nota in notas:
        c.drawString(100, y, f"{nota[0]}   {nota[1]}")
        y -= 20

    # Guarda el archivo PDF
    c.save()

    # Cierra el cursor y la conexión
    cursor.close()
    connection.close()

    # Muestra un mensaje de éxito
    print("Reporte Generado", f"El reporte ha sido generado correctamente. Nombre del archivo: {nombre_archivo}")


