import web

render = web.template.render('mvc/views/')

class BorrarProducto:
    def GET(self):
        # Aquí podrías obtener el producto por su ID desde tu modelo
        producto = {'id': 1, 'nombre': 'Producto de ejemplo', 'precio': 10.0}
        return render.borrar_producto(producto=producto)

    def POST(self):
        # Aquí podrías procesar la solicitud para borrar el producto con el ID proporcionado desde tu modelo
        return web.seeother('/')
