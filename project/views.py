from django.http import HttpResponse
import datetime

from django.template import Template, Context
from django.template.loader import get_template

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):

    p1=Persona("Profesor Juan", "Díaz")
    
    #nombre="Marco"
    #apellido="Padilla"

    temas_curso=["Plantillas","Modelos","Formularios","Vista","Despliegue"]

    ahora=datetime.datetime.now()

    #doc_externo=open("templates/mytemplate.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()

    doc_externo=get_template('mytemplate.html')

    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"comentario":"Este es un comentario","momento_actual":ahora,"temas":temas_curso})
    #documento=doc_externo.render(ctx)

    documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"comentario":"Este es un comentario","momento_actual":ahora,"temas":temas_curso})

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Chau")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad,agno):

    periodo=agno-2022
    edadFutura=edad+periodo
    documento="<body><h2>En el año %s tendrás %s años</h2></body></html>" %(agno,edadFutura)

    return HttpResponse(documento)