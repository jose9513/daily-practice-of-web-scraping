import sqlite3 as sql
import csv

def exportar_datos_para_bi():
    #Conectar a la base de datos
    conn = sql.connect('catalogo_bisuteria.db')
    with conn:
        cursor = conn.cursor()
        #ejecutar la consulta para obtener los datos
        cursor.execute("""SELECT * FROM joyas""")
        datos_joyas = cursor.fetchall()
        columnas_joyas = [descripcion[0] for descripcion in cursor.description]
        
        #Exportar los datos a un archivo CSV
        with open('datos_joyas.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            #Escribir los encabezados
            escritor.writerow(columnas_joyas)
            #Escribir los datos
            escritor.writerows(datos_joyas)
            
        print("Datos de joyas exportados correctamente a datos_joyas.csv")
            
        cursor.execute("""SELECT * FROM ventas""")
        datos_ventas = cursor.fetchall()
        columnas_ventas = [descripcion[0] for descripcion in cursor.description]
        
        #exportar los datos de las ventas a un archivo CSV
        with open('datos_ventas.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            #Escribir los encabezados
            escritor.writerow(columnas_ventas)
            #Escribir los datos
            escritor.writerows(datos_ventas)
            
        print("Datos de ventas exportados correctamente a datos_ventas.csv")
        
if __name__ == "__main__":
    exportar_datos_para_bi()
    print("Proceso de exportación de datos para Power BI completado.")