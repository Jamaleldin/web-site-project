from django.conf.urls import url
from . import views

app_name = 'teams'

urlpatterns = [
    url(r'^teams/$', views.Teamo.as_view(), name='index'),
]