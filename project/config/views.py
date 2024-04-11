from django.http import HttpResponse
from django.template import Context, Template


def saludo(request):
    return HttpResponse("¡Hola Django!")


def saludo_vista(request):
    return HttpResponse("<h1>Segunda vista</h1>")


def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")


def probando_template(request):
    mi_html = open("./templates/template1.html", encoding="UTF-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context({"saludo": "¡Bienvenido!", "autor": "Coderhouse"})
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)
