from django.conf.urls import url, include
from . import views

app_name='departments'

urlpatterns = [
    url(r'^computer/$', views.computer, name='computer'),
    url(r'^electric/$', views.electric, name='electric'),
    url(r'^mecha/$', views.mecha, name='mecha'),
]
