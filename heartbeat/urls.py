from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('heartbeat.views',
    url(r'^status/$', 'status'),
)
