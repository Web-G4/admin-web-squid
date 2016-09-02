from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from webPage.models import Rule, Privilege, Surfer, Content, RuleList, ActiveUser
from datetime import datetime
from django.http import HttpRequest

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import os

def squidConf():
    os.system("python squidConf/squidConf.py")
    os.system("python squidConf/listContents.py")
    os.system("python squidConf/listIps.py")
    os.system("squid -k reconfigure")

def admin_log_in(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        passField = request.POST['password']
        user = authenticate(username=username, password=passField)
        if user is not None:
            if user.is_active:
                login(request, user)
                squidConf()
                return redirect('/listaDeUsuarios/')
            else:
                pass
        else:
            pass
        squidConf()
    return render_to_response('activation.html',context)

def activatingUser(request):
    context = RequestContext(request)
    client_address = get_client_ip(request)
    try:
        activated = ActiveUser.objects.get(ipSurfer = client_address)
        return render_to_response('navegacion.html',{'user': activated},context)
    except ActiveUser.DoesNotExist:
        if request.method == 'POST':
            try:
                surfer = Surfer.objects.get(username = request.POST['username'], passField = request.POST['password'])
                ActiveUser.objects.filter(nameSurfer = surfer).delete()
                activated = ActiveUser()
                activated.nameSurfer = surfer
                activated.ipSurfer = client_address
                activated.save()
                squidConf()
                return render_to_response('navegacion.html',{'user': activated},context)
            except Surfer.DoesNotExist:
                print "No existe el usuario"
            except Surfer.MultipleObjectsReturned:
                print "Muchos usuarios!!!"
        squidConf()
        return render_to_response('activation.html',context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@login_required(login_url='/login/')
def listReglas(request):
    context = RequestContext(request)
    reglas = Rule.objects.all()
    lista = RuleList.objects.all()
    return render_to_response('listReglas.html',{'reglas':reglas,'lista':lista},context)

@login_required(login_url='/login/')
def listActiveUsers(request):
    context = RequestContext(request)
    users = ActiveUser.objects.all()
    return render_to_response('listActiveUsers.html',{'users': users},context)

@login_required(login_url='/login/')
def kickUser(request, idAU):
    context = RequestContext(request)
    user = ActiveUser.objects.get(idActiveUser = idAU)
    user.delete()
    users = Rule.objects.all()
    return render_to_response('listActiveUsers.html',{'users': users},context)

@login_required(login_url='/login/')
def delRegla(request, rId):
    context = RequestContext(request)
    rule = Rule.objects.get(idRule = rId)
    rule.delete()
    reglas = Rule.objects.all()
    privileges = Privilege.objects.all()
    return render_to_response('listReglas.html',{'reglas':reglas, 'privileges':privileges},context)

@login_required(login_url='/login/')
def modRegla(request, rId):
    context = RequestContext(request)
    privileges = Privilege.objects.all()
    contenidos = Content.objects.all()
    rule = Rule.objects.get(idRule = rId)
    if request.method == 'POST':
        print "is: "+str(request.POST['r_w'])
        if int(request.POST['r_w']):
            print request.POST['r_name']
            rule.nameURL = request.POST['r_name']
            rule.isContent = False
        else:
            print " hola "+request.POST['r_cont']
            rule.nameURL = request.POST['r_cont']
            rule.isContent = True
        if request.POST.getlist('r_is')==[u'1']:
            rule.allow = True
        else:
            rule.allow = False
        rule.description = request.POST['r_desc']
        rule.rFrom =  datetime.strptime(request.POST['r_s_h'], '%d %m %Y %H:%M')
        rule.rTo = datetime.strptime(request.POST['r_f_h'], '%d %m %Y %H:%M')
        rule.save()
        squidConf()
    return render_to_response('modRegla.html',{'contenidos':contenidos,'regla':rule, 'privilegios':privileges},context)

@login_required(login_url='/login/')
def addReglas(request):
    context = RequestContext(request)
    contenidos = Content.objects.all()
    privileges = Privilege.objects.all()
    if request.method == 'POST':
        rule = Rule()
        print "is: "+str(request.POST['r_w'])
        if int(request.POST['r_w']):
            print request.POST['r_name']
            rule.nameURL = request.POST['r_name']
            rule.isContent = False
        else:
            print " hola "+request.POST['r_cont']
            rule.nameURL = request.POST['r_cont']
            rule.isContent = True
        if request.POST.getlist('r_is')==[u'1']:
            rule.allow = True
        else:
            rule.allow = False
        rule.description = request.POST['r_desc']
        rule.rFrom =  datetime.strptime(request.POST['r_s_h'], '%d %m %Y %H:%M')
        rule.rTo = datetime.strptime(request.POST['r_f_h'], '%d %m %Y %H:%M')
        rule.save()
        lista = RuleList()
        priv = Privilege.objects.get(namePrivilege = request.POST['r_priv'])
        rule = Rule.objects.last()
        lista.privilegeAsigned = priv
        lista.ruleAsigned = rule
        lista.save()
        squidConf()
    return render_to_response('addReglas.html',{'contenidos':contenidos,'privilegios':privileges},context)

@login_required(login_url='/login/')
def addUsuario(request):
    context = RequestContext(request)
    privileges = Privilege.objects.all()
    if request.method=='POST':
        sur = Surfer()
        sur.username = request.POST['u_nom']
        sur.passField = request.POST['u_pass']
        sur.namePrivilege = Privilege.objects.get(namePrivilege=request.POST['u_priv'])
        sur.save()
        squidConf()
    return render_to_response('addUsuario.html',{'privilegios':privileges},context)

@login_required(login_url='/login/')
def listUsuarios(request):
    context = RequestContext(request)
    surfs = Surfer.objects.all()
    return render_to_response('listUsuarios.html',{'surfs':surfs},context)

@login_required(login_url='/login/')
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
        squidConf()
    return render_to_response('listPrivilegios.html',{'privilegios':privileges},context)

@login_required(login_url='/login/')
def addContenido(request):
    if request.method=='POST':
        cont = Content()
        cont.nameContent = request.POST['c_nom']
        cont.urlList = request.POST['c_text']
        cont.save()
    return render_to_response('contenido.html',context)
