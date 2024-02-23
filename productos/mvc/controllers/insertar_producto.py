import web


render = web.template.render('mvc/views/')

class InsertarProducto:
    def GET(self):
        return render.insertar_producto()
