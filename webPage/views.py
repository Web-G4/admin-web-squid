from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from webPage.models import Rule, Rulelist, Privilege, Surfer

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('index.html',
                              context)
def reglas(request):
    context = RequestContext(request)
    reglas = Rule.objects.all()
    privileges = Privilege.objects.all()
    #lista = RuleList.getObject(id=idLista)
    #reglas = lista.ruleasigned
    return render_to_response('reglas.html',{'reglas':reglas, 'privileges':privileges},
                              context)
def addReglas(request):
    context = RequestContext(request)
    return render_to_response('addReglas.html',
                              context)

def listaDeUsuarios(request):
    context = RequestContext(request)
    usuarios = Surfer.objects.all()
    privilegios = Privilege.objects.all()
    if request.method == "POST":
        id=request.POST.get('id')
        #suario_aux= Surfer.objects.get(id= id)
        print("MODIFICA LA BASE DE DATOS")
    return render_to_response('listaDeUsuarios.html',{'usuarios':usuarios,'privilegios':privilegios},context)

