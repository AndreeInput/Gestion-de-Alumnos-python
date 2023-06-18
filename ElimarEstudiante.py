import mysql.connector

# Función para eliminar un estudiante y sus notas asociadas
def eliminar_estudiante(estudiante):
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

    try:
        # Deshabilita temporalmente las restricciones de clave externa
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

        # Elimina las notas asociadas al estudiante
        consulta_notas = "DELETE FROM notas WHERE id_estudiante = %s"
        valores_notas = (id_estudiante,)
        cursor.execute(consulta_notas, valores_notas)

        # Elimina al estudiante
        consulta_estudiante = "DELETE FROM estudiantes WHERE id = %s"
        valores_estudiante = (id_estudiante,)
        cursor.execute(consulta_estudiante, valores_estudiante)

        # Confirma los cambios en la base de datos
        connection.commit()
        # Muestra un mensaje de éxito
        print("Eliminación Exitosa", "El estudiante y sus notas asociadas han sido eliminados.")
    except Exception as e:
        # Muestra un mensaje de error
        print("Error", str(e))
    finally:
        # Habilita nuevamente las restricciones de clave externa
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        # Cierra el cursor y la conexión
        cursor.close()
        connection.close()


