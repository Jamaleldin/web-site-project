from django.conf.urls import url
from . import views

app_name = 'union'

urlpatterns = [
    url(r'^union/$', views.Union.as_view(), name='index'),
]
