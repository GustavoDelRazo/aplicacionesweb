import web

render = web.template.render('mvc/views/')

class InsertarProducto:
    def GET(self):
        return render.insertar_producto()

    def POST(self):
        data = web.input()  # Obtener los datos del formulario
        # Aquí puedes agregar el código para insertar los datos en la base de datos
        # Por ejemplo:
        nombre = data.nombre
        precio = data.precio
        # Insertar lógica para agregar los datos a la base de datos
        return "Producto insertado correctamente: Nombre - {}, Precio - {}".format(nombre, precio)
