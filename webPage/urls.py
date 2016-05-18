from django.conf.urls import patterns, include, url
from webPage import views

urlpatterns = [
    url(r'^$', views.listaDeUsuarios, name='index'),
    url(r'reglas/$', views.reglas, name='reglas'),
    url(r'addReglas/$', views.addReglas, name='addReglas'),
    url(r'addUsuario/$', views.registro, name='registro'),
    #url(r'listaDeUsuarios/$', views.listaDeUsuarios, name='listaDeUsuarios'),
]
