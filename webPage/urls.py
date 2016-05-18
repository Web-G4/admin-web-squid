from django.conf.urls import patterns, include, url
from webPage import views

urlpatterns = [
    url(r'^$', views.listUsuarios, name='listUsuarios'),
    url(r'listReglas/$', views.listReglas, name='listReglas'),
    url(r'listPrivilegios/$', views.listPrivilegios, name='listPrivilegios'),
    url(r'addReglas/$', views.addReglas, name='addReglas'),
    url(r'addUsuario/$', views.addUsuario, name='addUsuario'),
    #url(r'listaDeUsuarios/$', views.listaDeUsuarios, name='listaDeUsuarios'),
]
