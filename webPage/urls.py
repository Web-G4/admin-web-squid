from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^$', 'webPage.views.index', name='index'),
    url(r'reglas/$', 'webPage.views.reglas', name='reglas'),
    url(r'addReglas/$', 'webPage.views.addReglas', name='addReglas'),
#    url(r'^listRules/(?P<idLista>[0-9]+)/$', 'webPage.views.reglas', name='listRule'),
)
