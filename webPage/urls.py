from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^$', 'webPage.views.index', name='index'),
    url(r'reglas-de-prueba/$', 'webPage.views.reglas', name='reglas'),
)
