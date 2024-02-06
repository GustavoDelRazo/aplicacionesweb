"""Framework web.py"""
import web

# Rutas de los controladore 
urls = (
    '/(.*)', 'mvc.controllers.hello.Hello'
)

app = web.application(urls, globals())

# Punto de entrada
if __name__ == "__main__":
    app.run()