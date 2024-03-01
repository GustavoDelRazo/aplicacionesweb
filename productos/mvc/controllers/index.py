import web

render = web.template.render('mvc/views/')

class Index:
    def GET(self):
        # Aquí podrías obtener la lista de productos desde tu modelo
        productos = []
        return render.lista_productos()
