from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from webPage.models import Rule, Privilege, Surfer, Content
from datetime import datetime

def listReglas(request):
    context = RequestContext(request)
    reglas = Rule.objects.all()
    privileges = Privilege.objects.all()
    #lista = RuleList.getObject(id=idLista)
    #reglas = lista.ruleasigned
    return render_to_response('listReglas.html',{'reglas':reglas, 'privileges':privileges},context)

def delRegla(request, rId):
    context = RequestContext(request)
    rule = Rule.objects.get(idRule = rId)
    rule.delete()
    reglas = Rule.objects.all()
    privileges = Privilege.objects.all()
    return render_to_response('listReglas.html',{'reglas':reglas, 'privileges':privileges},context)

def modRegla(request, rId):
    context = RequestContext(request)
    contenidos = Content.objects.all()
    rule = Rule.objects.get(idRule = rId)
    if request.method == 'POST':
        if request.POST['r_w']:
            print request.POST['r_name']
            rule.nameURL = request.POST['r_name']
            rule.isContent = False
        else:
            print request.POST['r_desc']
            rule.nameURL = request.POST['r_desc']
            rule.isContent = True
        if request.POST.getlist('r_is')==[u'1']:
            rule.allow = True
        else:
            rule.allow = False
        rule.description = request.POST['r_desc']
        rule.rFrom =  datetime.strptime(request.POST['r_s_h'], '%d %m %Y %H:%M')
        rule.rTo = datetime.strptime(request.POST['r_f_h'], '%d %m %Y %H:%M')
        rule.save()
    return render_to_response('modRegla.html',{'contenidos':contenidos,'regla':rule},context)

def addReglas(request):
    context = RequestContext(request)
    contenidos = Content.objects.all()
    if request.method == 'POST':
        rule = Rule()
        if request.POST['r_w']:
            print request.POST['r_name']
            rule.nameURL = request.POST['r_name']
            rule.isContent = False
        else:
            print request.POST['r_desc']
            rule.nameURL = request.POST['r_desc']
            rule.isContent = True
        if request.POST.getlist('r_is')==[u'1']:
            rule.allow = True
        else:
            rule.allow = False
        rule.description = request.POST['r_desc']
        rule.rFrom =  datetime.strptime(request.POST['r_s_h'], '%d %m %Y %H:%M')
        rule.rTo = datetime.strptime(request.POST['r_f_h'], '%d %m %Y %H:%M')
        rule.save()
    return render_to_response('addReglas.html',{'contenidos':contenidos},context)

def addUsuario(request):
    context = RequestContext(request)
    privileges = Privilege.objects.all()
    if request.method=='POST':
        sur = Surfer()
        sur.username = request.POST['u_nom']
        sur.passField = request.POST['u_pass']
        sur.namePrivilege = Privilege.objects.get(namePrivilege=request.POST['u_priv'])
        sur.save()
    return render_to_response('addUsuario.html',{'privilegios':privileges},context)

def listUsuarios(request):
    context = RequestContext(request)
    surfs = Surfer.objects.all()
    return render_to_response('listUsuarios.html',{'surfs':surfs},context)

def listPrivilegios(request):
    context = RequestContext(request)
    privileges = Privilege.objects.all()
    if request.method=='POST':
        priv = Privilege()
        priv.namePrivilege = request.POST['p_nom']
        if request.POST.getlist('p_is')==[u'1']:
            priv.isBlock = True
        else:
            priv.isBlock = False
        priv.save()
    return render_to_response('listPrivilegios.html',{'privilegios':privileges},context)


