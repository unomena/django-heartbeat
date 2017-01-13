from django.conf.urls import url

from heartbeat import views

urlpatterns = [
    url(r'^status/$', views.status, name='heartbeat_status'),
]
