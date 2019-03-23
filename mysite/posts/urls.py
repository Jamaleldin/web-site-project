from django.conf.urls import url, include
from . import views

app_name='posts'

urlpatterns = [
    url(r'^$', views.post_list , name='post_list'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<id>\d+)/$', views.post_detail , name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='post_update'),
]
