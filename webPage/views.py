from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from webPage.models import Rule, Rulelist, Privilege, Surfer, Content
from datetime import datetime

def listReglas(request):
    context = RequestContext(request)
    reglas = Rule.objects.all()
    privileges = Privilege.objects.all()
    #lista = RuleList.getObject(id=idLista)
    #reglas = lista.ruleasigned
    return render_to_response('listReglas.html',{'reglas':reglas, 'privileges':privileges},context)

def addReglas(request):
    context = RequestContext(request)
    contenidos = Content.objects.all()
    if request.method == 'POST':
        rule = Rule()
        if request.POST['r_name'] == "":
            rule.nameurl = request.POST['r_name']
            rule.iscontent = False
        else:
            #rule.nameurl = request.POST['r_cont']
            rule.iscontent = True
        if request.POST.getlist('r_is')==[u'1']:
            rule.allow = True
        else:
            rule.allow = False
        rule.description = request.POST['r_desc']
        rule.rfrom =  datetime.strptime(request.POST['r_s_h'], '%d %m %Y %H:%M')
        rule.rto = datetime.strptime(request.POST['r_f_h'], '%d %m %Y %H:%M')
        rule.save()
    return render_to_response('addReglas.html',{'contenidos':contenidos},context)

def addUsuario(request):
    context = RequestContext(request)
    privileges = Privilege.objects.all()
    if request.method=='POST':
        sur = Surfer()
        sur.username = request.POST['u_nom']
        sur.pass_field = request.POST['u_pass']
        sur.nameprivilege = Privilege.objects.get(nameprivilege=request.POST['u_priv'])
        sur.save()
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


