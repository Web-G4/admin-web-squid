from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from webPage.models import Rule, Rulelist, Privilege, Surfer

def listReglas(request):
    context = RequestContext(request)
    reglas = Rule.objects.all()
    privileges = Privilege.objects.all()
    #lista = RuleList.getObject(id=idLista)
    #reglas = lista.ruleasigned
    return render_to_response('listReglas.html',{'reglas':reglas, 'privileges':privileges},context)

def addReglas(request):
    context = RequestContext(request)
    return render_to_response('addReglas.html',context)

def addUsuario(request):
    context = RequestContext(request)
    privileges = Privilege.objects.all()
    return render_to_response('addUsuario.html',{'privilegios':privileges},context)

def listUsuarios(request):
    context = RequestContext(request)
    usuarios = Surfer.objects.all()
    return render_to_response('listUsuarios.html',{'usuarios':usuarios},context)

def listPrivilegios(request):
    context = RequestContext(request)
    privileges = Privilege.objects.all()
    if request.method=='POST':
        priv = Privilege()
        priv.nameprivilege = request.POST['p_nom']
        if request.POST.getlist('p_is')==[u'1']:
            priv.isblock = True
        else:
            priv.isblock = False
        priv.save()
    return render_to_response('listPrivilegios.html',{'privilegios':privileges},context)


