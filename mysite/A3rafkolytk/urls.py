from django.conf.urls import url, include
from . import views

app_name = 'A3rafkolytk'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
