import web

render = web.template.render('mvc/controllers/views/')

class Index:
    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        try:
            num1 = float(form.num1)
            num2 = float(form.num2)
            result = num1 + num2
            return f"El resultado de la suma es: {result}"
        except ValueError:
            return "Error: Por favor, ingresa números válidos."
