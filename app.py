from flask import Flask, render_template, request, send_file
import pyodbc
import pandas as pd
import io

app = Flask(__name__)

# Configuración de la conexión
server = 'SERVERINSAC5\\WINCAJASERVER'
database = 'Ferretianguis'
username = 'sa'
password = 'Wincaja20'

@app.route('/')
def index():
    articulo = request.args.get('articulo', '')
    nombre = request.args.get('nombre', '')
    codigo_barras = request.args.get('codigo_barras', '')
    descripcion_subfamilia = request.args.get('descripcion_subfamilia', '')

    try:
        # Cadena de conexión
        connection_string = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';'
            'DATABASE=' + database + ';'
            'UID=' + username + ';'
            'PWD=' + password
        )

        # Crear un cursor para ejecutar las consultas
        cursor = connection_string.cursor()

        # Construir la consulta SQL con JOIN
        query = '''
            SELECT 
                a.Articulo,
                a.CodigoBarras,
                a.Subfamilia,
                a.Nombre,
                s.Descripcion AS SubfamiliaDescripcion
            FROM Articulos a
            LEFT JOIN Subfamilias s ON a.Subfamilia = s.Subfamilia
            WHERE 1=1
        '''
        params = []

        if articulo:
            query += " AND a.Articulo LIKE ?"
            params.append('%' + articulo + '%')
        if nombre:
            query += " AND a.Nombre LIKE ?"
            params.append('%' + nombre + '%')
        if codigo_barras:
            query += " AND a.CodigoBarras LIKE ?"
            params.append('%' + codigo_barras + '%')
        if descripcion_subfamilia:
            query += " AND s.Descripcion LIKE ?"
            params.append('%' + descripcion_subfamilia + '%')

        cursor.execute(query, params)

        # Obtener todos los resultados de la consulta
        rows = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection_string.close()

        # Pasar los resultados y los filtros a la plantilla HTML
        return render_template(
            'index.html', 
            rows=rows, 
            articulo=articulo, 
            nombre=nombre, 
            codigo_barras=codigo_barras,
            descripcion_subfamilia=descripcion_subfamilia
        )

    except Exception as e:
        return f"Error al intentar conectar o ejecutar la consulta: {e}"


@app.route('/proveedores/<articulo>')
def proveedores(articulo):
    try:
        # Conectar a la base de datos
        connection_string = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';'
            'DATABASE=' + database + ';'
            'UID=' + username + ';'
            'PWD=' + password
        )

        # Crear un cursor para ejecutar la consulta
        cursor = connection_string.cursor()

        # Consulta para obtener los proveedores relacionados con el artículo
        query = '''
            SELECT 
                Articulo, 
                Proveedor, 
                NombreProvedor,
                DescAlmacen
            FROM ArticulosyProveedores
            WHERE DescAlmacen='Acedis' AND Articulo = ?
        '''
        cursor.execute(query, (articulo,))

        # Obtener los resultados
        rows = cursor.fetchall()

        # Cerrar conexión
        cursor.close()
        connection_string.close()

        # Renderizar la plantilla de proveedores
        return render_template('proveedores.html', rows=rows, articulo=articulo)

    except Exception as e:
        return f"Error al intentar conectar o ejecutar la consulta: {e}"


@app.route('/precios1/<articulo>')
def precios1(articulo):
    try:
        # Conectar a la base de datos
        connection_string = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';'
            'DATABASE=' + database + ';'
            'UID=' + username + ';'
            'PWD=' + password
        )

        # Crear un cursor para ejecutar la consulta
        cursor = connection_string.cursor()

        # Consulta para obtener los precios de la tabla Qv4PreciosNo1
        query = '''
            SELECT 
                TipoTiendaDescripcion, 
                Precio1IVAUV
            FROM Qv4PreciosNo1
            WHERE Articulo = ?
        '''
        cursor.execute(query, (articulo,))

        # Obtener los resultados
        rows = cursor.fetchall()

        # Cerrar conexión
        cursor.close()
        connection_string.close()

        # Renderizar la plantilla de precios
        return render_template('precios1.html', rows=rows, articulo=articulo)

    except Exception as e:
        return f"Error al intentar conectar o ejecutar la consulta: {e}"
@app.route('/precios2/<articulo>')
def precios2(articulo):
    try:
        # Conectar a la base de datos
        connection_string = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';'
            'DATABASE=' + database + ';'
            'UID=' + username + ';'
            'PWD=' + password
        )

        # Crear un cursor para ejecutar la consulta
        cursor = connection_string.cursor()

        # Consulta para obtener los precios de la tabla Qv4PreciosNo1
        query = '''
            SELECT 
                TipoTiendaDescripcion, 
                Precio2IVAUV
            FROM Qv4PreciosNo2
            WHERE Articulo = ?
        '''
        cursor.execute(query, (articulo,))

        # Obtener los resultados
        rows = cursor.fetchall()

        # Cerrar conexión
        cursor.close()
        connection_string.close()

        # Renderizar la plantilla de precios
        return render_template('precios2.html', rows=rows, articulo=articulo)

    except Exception as e:
        return f"Error al intentar conectar o ejecutar la consulta: {e}"

@app.route('/precios3/<articulo>')
def precio3(articulo):
    try:
        # Conectar a la base de datos
        connection_string = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';'
            'DATABASE=' + database + ';'
            'UID=' + username + ';'
            'PWD=' + password
        )

        # Crear un cursor para ejecutar la consulta
        cursor = connection_string.cursor()

        # Consulta para obtener los precios de la tabla Qv4PreciosNo1
        query = '''
            SELECT 
                TipoTiendaDescripcion, 
                Precio3IVAUV
            FROM Qv4PreciosNo3
            WHERE Articulo = ?
        '''
        cursor.execute(query, (articulo,))

        # Obtener los resultados
        rows = cursor.fetchall()

        # Cerrar conexión
        cursor.close()
        connection_string.close()

        # Renderizar la plantilla de precios
        return render_template('precios3.html', rows=rows, articulo=articulo)

    except Exception as e:
        return f"Error al intentar conectar o ejecutar la consulta: {e}"
    
@app.route('/preneto/<articulo>')
def precioNeto(articulo):
    try:
        # Conectar a la base de datos
        connection_string = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';'
            'DATABASE=' + database + ';'
            'UID=' + username + ';'
            'PWD=' + password
        )

        # Crear un cursor para ejecutar la consulta
        cursor = connection_string.cursor()

        # Consulta para obtener los proveedores relacionados con el artículo 
        query = '''
            SELECT 
                Articulo, 
                TipoTienda, 
                UltimoCostoNeto,
                DescAlmacen
            FROM QV4ListaPrecioConCosto
            WHERE DescAlmacen='Acedis' AND TipoTienda='1' AND Articulo = ?
        '''
        cursor.execute(query, (articulo,))

        # Obtener los resultados
        rows = cursor.fetchall()

        # Cerrar conexión
        cursor.close()
        connection_string.close()

        # Renderizar la plantilla de proveedores
        return render_template('precioNeto.html', rows=rows, articulo=articulo)

    except Exception as e:
        return f"Error al intentar conectar o ejecutar la consulta: {e}"

@app.route('/compras/<articulo>')
def compras(articulo):
    try:
        # Conectar a la base de datos
        connection_string = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';'
            'DATABASE=' + database + ';'
            'UID=' + username + ';'
            'PWD=' + password
        )

        # Crear un cursor para ejecutar la consulta
        cursor = connection_string.cursor()

        # Consulta para obtener los proveedores relacionados con el artículo 
        query = '''
            SELECT 
                Articulo, 
                Cantidad, 
                ValorCosto,
                IVA,
                ValorCostoNeto
            FROM QxxDetalleCompra
            WHERE Articulo = ?
        '''
        cursor.execute(query, (articulo,))

        # Obtener los resultados
        rows = cursor.fetchall()

        # Cerrar conexión
        cursor.close()
        connection_string.close()

        # Renderizar la plantilla de proveedores
        return render_template('compras.html', rows=rows, articulo=articulo)

    except Exception as e:
        return f"Error al intentar conectar o ejecutar la consulta: {e}"
    
@app.route('/ventas/<articulo>')
def ventas(articulo):
    try:
        # Conectar a la base de datos
        connection_string = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';'
            'DATABASE=' + database + ';'
            'UID=' + username + ';'
            'PWD=' + password
        )

        # Crear un cursor para ejecutar la consulta
        cursor = connection_string.cursor()

        # Consulta para obtener los proveedores relacionados con el artículo 
        query = '''
            SELECT 
                Articulo, 
                NombreArticulo,
                NombreProvedor,
                VentaUnidadPeriodo,
                VentaValorAnual, 
                VentaValorPeriodo,
                VentaValorCostoAnual
            FROM ArticulosyProveedores
            WHERE DescAlmacen='Acedis' AND Articulo = ?
        '''
        cursor.execute(query, (articulo,))

        # Obtener los resultados
        rows = cursor.fetchall()

        # Cerrar conexión
        cursor.close()
        connection_string.close()

        # Renderizar la plantilla de proveedores
        return render_template('ventas.html', rows=rows, articulo=articulo)

    except Exception as e:
        return f"Error al intentar conectar o ejecutar la consulta: {e}"
    

if __name__ == '__main__':
    app.run(debug=True)


