from django.conf.urls import url
from . import views

app_name = 'technical'

urlpatterns = [
    url(r'^technical/$', views.Techo.as_view(), name='index'),
]