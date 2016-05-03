from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from webPage.models import Rule

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('index.html',
                              context)
def reglas(request):
    context = RequestContext(request)
    reglas = Rule.objects.all()
    return render_to_response('reglas.html',{'reglas':reglas},
                              context)
def addReglas(request):
    context = RequestContext(request)
    return render_to_response('addReglas.html',
                              context)
