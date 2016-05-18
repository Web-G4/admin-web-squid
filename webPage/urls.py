from django.conf.urls import patterns, include, url
from webPage import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'reglas/$', views.reglas, name='reglas'),
    url(r'addReglas/$', views.addReglas, name='addReglas'),
    url(r'listaDeUsuarios/$', listaDeUsuarios, name='listaDeUsuarios'),
    url(r'addUsuario/$', views.registro, name='registro'),
    #    url(r'^listRules/(?P<idLista>[0-9]+)/$', 'webPage.views.reglas', name='listRule'),
]
