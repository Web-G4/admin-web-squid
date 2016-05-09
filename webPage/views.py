from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from webPage.models import Rule, Rulelist, Privilege

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


