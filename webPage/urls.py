from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'webPage.views.index', name='index'),
                      )
