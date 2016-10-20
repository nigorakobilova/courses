from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.courses),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^deleteCourse/(?P<id>\d+)$', views.deleteCourse)
]
