import web

render = web.template.render('mvc/views/')

class InsertarProducto:
    def GET(self):
        return render.insertar_producto()

    def POST(self):
        # Aquí podrías procesar los datos del formulario para insertar un nuevo producto en tu modelo
        return web.seeother('/')
