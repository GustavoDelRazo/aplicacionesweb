import web
from mvc.controllers.models.calcu import Calcu

render = web.template.render('mvc/controllers/views/', base='calcus')

class Calculadora:
    def GET(self):
        try:
            return render.calculadora(resultado=None)
        except Exception as e:
            print(f"Error 101 - index {e.args}")
            return "Upsi algo salió mal"

    def POST(self):
        try:
            data = web.input()
            numero1 = int(data.numero1)
            numero2 = int(data.numero2)
            resultado = Calcu.sumar(numero1, numero2)
            return render.calculadora(resultado=resultado)
        except Exception as e:
            print(f"Error 102 - index {e.args}")
            return "Upsi algo salió mal"