import web

render = web.template.render('mvc/views/')

class VerProducto:
    def GET(self):
        # Aquí podrías obtener el producto por su ID desde tu modelo
        producto = {'id': 1, 'nombre': 'Producto de ejemplo', 'precio': 10.0}
        return render.ver_producto(producto=producto)
