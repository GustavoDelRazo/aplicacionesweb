import web

render = web.template.render('mvc/views/')

class Index:
    def GET(self):
        # Aquí podrías obtener la lista de productos desde tu modelo
        # Por ejemplo, simulando una lista de productos:
        lista_de_productos = [
            {"nombre": "Producto 1", "precio": 10},
            {"nombre": "Producto 2", "precio": 20},
            {"nombre": "Producto 3", "precio": 30}
        ]
        return render.lista_productos(lista_de_productos)
