from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from example import views

urlpatterns = [

     # re_path(r'^example_lista/$', views.ExampleList.as_view() ),
     # re_path(r'^example_detail/(?P<id>\d+)$', views.ExampleDetail.as_view() ),
     #x
     
     #urls extra
     re_path(r'^lista_actividades/$', views.ActividadList.as_view() ),
     #re_path(r'^listaiproductos/$', views.InventoriesFList.as_view() ),
     re_path(r'^detalle_actividad/(?P<id>\d+)$', views.CosaDetail.as_view() ),
     re_path(r'^lista_cosa/(?P<id>\d+)$', views.CosaListA.as_view() ),
     re_path(r'^add_actividades/$', views.ActividadList.as_view() ),
     
]