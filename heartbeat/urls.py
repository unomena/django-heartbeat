from django.conf.urls import patterns, url

urlpatterns = patterns('heartbeat.views',
    url(r'^status/$', 'status'),
)
