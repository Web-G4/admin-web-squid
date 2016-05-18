from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from webPage.models import Rule, Rulelist, Privilege, Surfer

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

def registro(request):
    context = RequestContext(request)
    users = Rule.objects.all()
    return render_to_response('registro.html', {'users':users},
                              context)

def listaDeUsuarios(request):
    context = RequestContext(request)
    usuarios = Surfer.objects.all()
    return render_to_response('listaDeUsuarios.html',{'usuarios':usuarios},context)


