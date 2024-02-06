"""Framework web.py"""
import web

# Rutas de los controladore 
urls = (
    '/', 'mvc.controllers.hello.Hello',
    "/pagina2", "mvc.controllers.pagina2.Pagina2"
)

app = web.application(urls, globals())

# Punto de entrada
if __name__ == "__main__":
    app.run()