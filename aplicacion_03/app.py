"""Framework web.py"""
import web

# Rutas de los controladore 
urls = (
    '/', 'mvc.controllers.index.Index'
)

app = web.application(urls, globals())

# Punto de entrada
if __name__ == "__main__":
    app.run()