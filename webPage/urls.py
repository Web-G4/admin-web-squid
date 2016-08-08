from django.conf.urls import patterns, include, url
from webPage import views

urlpatterns = [
    url(r'listaDeUsuarios/$', views.listUsuarios, name='listUsuarios'),
    url(r'listReglas/$', views.listReglas, name='listReglas'),
    url(r'listPrivilegios/$', views.listPrivilegios, name='listPrivilegios'),
    url(r'addReglas/$', views.addReglas, name='addReglas'),
    url(r'addUsuario/$', views.addUsuario, name='addUsuario'),
    url(r'login/$', views.admin_log_in, name='login'),
    url(r'^$', views.activatingUser, name='activatingUser'),
    url(r'^modRegla/(?P<rId>[0-9]+)/$', views.modRegla, name='modRegla'),
    url(r'^delRegla/(?P<rId>[0-9]+)/$', views.delRegla, name='delRegla'),
    #url(r'listaDeUsuarios/$', views.listaDeUsuarios, name='listaDeUsuarios'),
]
