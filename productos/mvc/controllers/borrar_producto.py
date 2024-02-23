import web

render = web.template.render('mvc/views/')

class BorrarProducto:
    def GET(self):
        return render.borrar_producto()
