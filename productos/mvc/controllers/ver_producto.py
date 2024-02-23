import web

render = web.template.render('mvc/views/')

class VerProducto:
    def GET(self):
        # Aquí podrías obtener el producto por su ID desde tu modelo
        return render.ver_producto()
