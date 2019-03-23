from django.conf.urls import url, include
from . import views

app_name='comments'

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.comment_thread , name='comment_thread'),
]
